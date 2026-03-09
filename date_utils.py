"""Date utilities"""

from __future__ import annotations

# cSpell: ignore fstring
# pylint: disable=W0611,C0411,logging-fstring-interpolation
import datetime as dt

import pandas as pd

from ionbus_utils.regex_utils import NON_DIGIT_RE


def yyyymmdd_to_date(string: str | None) -> dt.date | None:
    """Converts a string of format yyyyy-mm-dd to a date object.
    All punctuation/non digits are ignored if a string is passed.
    An empty string or non will have None returned"""
    return (
        dt.datetime.strptime(NON_DIGIT_RE.sub("", string), "%Y%m%d").date()
        if string
        else None
    )


def to_date(
    the_date: dt.date | dt.datetime | pd.Timestamp | str | None,
) -> dt.date | None:
    """Returns date (if date/time object) or None"""
    if not the_date:
        return None
    return pd.Timestamp(the_date).date()


def to_date_isoformat(
    the_date: dt.date | dt.datetime | pd.Timestamp | str | None,
    no_symbols: bool = False,
) -> str | None:
    """Returns date in isoformat string (if date/time object) or None"""
    if (date_obj := to_date(the_date)) is None:
        return None
    ret_val = date_obj.isoformat()
    return ret_val.replace("-", "") if no_symbols else ret_val


def first_day_of_next_month(
    the_date: dt.date | dt.datetime | pd.Timestamp | str,
) -> dt.date:
    """returns a date 1st of next month"""
    new_date = to_date(the_date)
    if not new_date:
        raise RuntimeError("Most provide valid date")
    return dt.date(
        (
            new_date.year + 1
            if new_date.month == 12  # noqa: PLR2004
            else new_date.year
        ),
        new_date.month % 12 + 1,
        1,
    )


def first_day_of_month(
    the_date: dt.date | dt.datetime | pd.Timestamp | str,
) -> dt.date:
    """returns first day of this month"""
    new_date = to_date(the_date)
    if not new_date:
        raise RuntimeError("Most provide valid date")
    return dt.date(
        new_date.year,
        new_date.month,
        1,
    )


def last_day_of_month(
    the_date: dt.date | dt.datetime | pd.Timestamp | str,
) -> dt.date:
    """returns last day of this month"""
    return first_day_of_next_month(the_date) - dt.timedelta(days=1)


# Tools for generation partition strings for different types of
# date partitions


def ensure_date_is_iso_string(
    the_date: dt.date | dt.datetime | pd.Timestamp | str | None,
) -> str | None:
    """Converts date to year-week string.  If None passed
    in, None is returned"""
    if not the_date:
        return None
    return pd.Timestamp(the_date).date().isoformat()


# Valid date partition granularities for Hive-style partitioning
DATE_PARTITION_GRANULARITIES = ("day", "week", "month", "quarter", "year")


def date_partition_value(date: dt.date, granularity: str) -> str:
    """
    Generate a Hive-style partition value string for a date.

    Creates partition values suitable for Hive-partitioned directories
    (e.g., "month=M2024-01/").

    Args:
        date: The date to generate a partition value for.
        granularity: One of "day", "week", "month", "quarter", "year".

    Returns:
        Partition value string formatted as:
        - day: "2024-01-15" (ISO format)
        - week: "W2024-03" (ISO week number)
        - month: "M2024-01"
        - quarter: "Q2024-1"
        - year: "Y2024"

    Raises:
        ValueError: If granularity is not valid.

    Examples:
        >>> date_partition_value(dt.date(2024, 1, 15), "month")
        'M2024-01'
        >>> date_partition_value(dt.date(2024, 1, 15), "week")
        'W2024-03'
    """
    if granularity not in DATE_PARTITION_GRANULARITIES:
        raise ValueError(
            f"Invalid granularity '{granularity}'. "
            f"Must be one of: {DATE_PARTITION_GRANULARITIES}"
        )

    if granularity == "day":
        return date.isoformat()

    if granularity == "week":
        iso_year, iso_week, _ = date.isocalendar()
        return f"W{iso_year}-{iso_week:02d}"

    if granularity == "month":
        return f"M{date.year}-{date.month:02d}"

    if granularity == "quarter":
        quarter = (date.month - 1) // 3 + 1
        return f"Q{date.year}-{quarter}"

    if granularity == "year":
        return f"Y{date.year}"

    # Should not reach here due to earlier validation
    raise ValueError(f"Unhandled granularity: {granularity}")


def date_partition_range(
    partition_value: str, granularity: str
) -> tuple[dt.date, dt.date]:
    """
    Get the date range covered by a partition value.

    Given a partition value string (e.g., "M2024-01"), returns the
    start and end dates of that partition period.

    Args:
        partition_value: Partition value string (e.g., "Y2024", "M2024-01").
        granularity: One of "day", "week", "month", "quarter", "year".

    Returns:
        Tuple of (start_date, end_date) for the partition period.

    Raises:
        ValueError: If partition_value format doesn't match granularity.

    Examples:
        >>> date_partition_range("M2024-01", "month")
        (datetime.date(2024, 1, 1), datetime.date(2024, 1, 31))
        >>> date_partition_range("Y2024", "year")
        (datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    """
    if granularity == "day":
        date = dt.date.fromisoformat(partition_value)
        return (date, date)

    if granularity == "week":
        # Format: W2024-03
        year = int(partition_value[1:5])
        week = int(partition_value[6:])
        # ISO week: Monday is day 1
        jan4 = dt.date(year, 1, 4)
        start_of_year = jan4 - dt.timedelta(days=jan4.weekday())
        week_start = start_of_year + dt.timedelta(weeks=week - 1)
        week_end = week_start + dt.timedelta(days=6)
        return (week_start, week_end)

    if granularity == "month":
        # Format: M2024-01
        year = int(partition_value[1:5])
        month = int(partition_value[6:])
        start = dt.date(year, month, 1)
        # End of month
        if month == 12:
            end = dt.date(year + 1, 1, 1) - dt.timedelta(days=1)
        else:
            end = dt.date(year, month + 1, 1) - dt.timedelta(days=1)
        return (start, end)

    if granularity == "quarter":
        # Format: Q2024-1
        year = int(partition_value[1:5])
        quarter = int(partition_value[6:])
        start_month = (quarter - 1) * 3 + 1
        end_month = quarter * 3
        start = dt.date(year, start_month, 1)
        if end_month == 12:
            end = dt.date(year + 1, 1, 1) - dt.timedelta(days=1)
        else:
            end = dt.date(year, end_month + 1, 1) - dt.timedelta(days=1)
        return (start, end)

    if granularity == "year":
        # Format: Y2024
        year = int(partition_value[1:])
        return (dt.date(year, 1, 1), dt.date(year, 12, 31))

    raise ValueError(f"Invalid granularity: {granularity}")
