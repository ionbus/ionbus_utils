@echo off
REM Build and publish ionbus-utils to PyPI and Anaconda.
REM Prereqs: activate an env that has: build, twine, conda-build, anaconda-client.
REM Auth: %USERPROFILE%\.pypirc for PyPI, `anaconda login` for Anaconda.
REM Run `release.bat --help` for full option list.

setlocal enabledelayedexpansion

set "ANACONDA_USER=ionbus"
set "DO_TAG=0"
set "TEST_PYPI=0"
set "CONDA_ONLY=0"
set "PIP_ONLY=0"
set "SKIP_PIP=0"
set "ANY_BRANCH=0"

:parse_args
if "%~1"=="" goto after_args
if /i "%~1"=="-h"            goto :show_help
if /i "%~1"=="--help"        goto :show_help
if /i "%~1"=="/?"            goto :show_help
if /i "%~1"=="--tag"         (set "DO_TAG=1" & shift & goto parse_args)
if /i "%~1"=="--test"        (set "TEST_PYPI=1" & shift & goto parse_args)
if /i "%~1"=="--conda-only"  (set "CONDA_ONLY=1" & shift & goto parse_args)
if /i "%~1"=="--pip-only"    (set "PIP_ONLY=1" & shift & goto parse_args)
if /i "%~1"=="--skip-pip"    (set "SKIP_PIP=1" & shift & goto parse_args)
if /i "%~1"=="--any-branch"  (set "ANY_BRANCH=1" & shift & goto parse_args)
echo Unknown arg: %~1 1>&2
echo Run with --help for usage. 1>&2
exit /b 2
:after_args

if "%PIP_ONLY%"=="1" if "%CONDA_ONLY%"=="1" (
    echo ERROR: --pip-only and --conda-only are mutually exclusive. 1>&2
    exit /b 2
)

cd /d "%~dp0"

echo === Verifying branch ===
for /f "delims=" %%b in ('git branch --show-current') do set "CURRENT_BRANCH=%%b"
if not "%ANY_BRANCH%"=="1" if not "!CURRENT_BRANCH!"=="main" (
    echo ERROR: on branch '!CURRENT_BRANCH!', not 'main'. Use --any-branch to override. 1>&2
    exit /b 1
)
echo Branch: !CURRENT_BRANCH!

if "%DO_TAG%"=="1" (
    echo === Running auto_tag ===
    python git_utils\auto_tag.py . --throw-on-failure
    if errorlevel 1 goto :fail
)

echo === Verifying HEAD is tagged ===
for /f "delims=" %%t in ('git describe --exact-match --tags HEAD 2^>nul') do set "TAG=%%t"
if not defined TAG (
    echo ERROR: HEAD is not tagged. Create a new tag ^(e.g. re-run with --tag^). 1>&2
    exit /b 1
)
echo HEAD tag: !TAG!

echo === Cleaning previous build artifacts ===
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
for /d %%D in (*.egg-info) do rmdir /s /q "%%D"

if "%CONDA_ONLY%"=="1" (
    echo === Skipping pip build+upload ^(--conda-only^) ===
) else (
    echo === Building pip wheel ===
    python -m build --wheel
    if errorlevel 1 goto :fail

    if "%SKIP_PIP%"=="1" (
        echo === Skipping pip upload ^(--skip-pip^) ===
    ) else if "%TEST_PYPI%"=="1" (
        echo === Uploading to TestPyPI ===
        python -m twine upload --repository testpypi dist/*
        if errorlevel 1 goto :fail
    ) else (
        echo === Uploading to PyPI ===
        python -m twine upload dist/*
        if errorlevel 1 goto :fail
    )
)

if "%PIP_ONLY%"=="1" (
    echo === Skipping conda build+upload ^(--pip-only^) ===
    echo === Done: released !TAG! ^(pip only^) ===
    endlocal
    exit /b 0
)

REM Force win-64 solver on Windows ARM (conda-forge lacks win-arm64 python).
REM Harmless on native x64.
set "CONDA_SUBDIR=win-64"

echo === Resolving conda output path ===
for /f "delims=" %%i in ('conda build conda-recipe -c conda-forge --output') do set "CONDA_PKG=%%i"
echo Will build: !CONDA_PKG!

echo === Building conda package ===
conda build conda-recipe -c conda-forge
if errorlevel 1 goto :fail

REM Locate anaconda-client. Not on PATH when running from a non-base env,
REM so fall back to the miniforge install location.
set "ANACONDA_EXE=anaconda"
where anaconda >nul 2>&1
if errorlevel 1 (
    if exist "%USERPROFILE%\miniforge3\Scripts\anaconda.exe" (
        set "ANACONDA_EXE=%USERPROFILE%\miniforge3\Scripts\anaconda.exe"
    ) else (
        echo ERROR: anaconda-client not found. Install with: 1>&2
        echo   conda install -n base -c conda-forge anaconda-client -y 1>&2
        goto :fail
    )
)

echo === Uploading to Anaconda (user: %ANACONDA_USER%) ===
"!ANACONDA_EXE!" upload --user %ANACONDA_USER% "!CONDA_PKG!"
if errorlevel 1 goto :fail

echo === Done: released !TAG! ===
endlocal
exit /b 0

:show_help
echo.
echo Usage: release.bat [options]
echo.
echo Builds and publishes ionbus-utils to PyPI and Anaconda.
echo.
echo By default: requires HEAD to be tagged, then builds+uploads BOTH the
echo pip wheel (to PyPI) and the conda package (to Anaconda user "ionbus").
echo.
echo Options:
echo   -h, --help      Show this help and exit.
echo   --tag           Before building, run auto_tag to create and push a
echo                   new tag from commit-message hashtags (#Major/
echo                   #Minor/#Inc/#Fix/#RC/#Prod).
echo   --test          Upload the pip wheel to TestPyPI instead of PyPI.
echo                   No effect with --conda-only.
echo   --pip-only      Build and upload ONLY the pip wheel. Skip the
echo                   conda build and Anaconda upload entirely.
echo   --conda-only    Build and upload ONLY the conda package. Skip the
echo                   pip wheel build and PyPI upload entirely.
echo   --skip-pip      Build the pip wheel but do not upload it. The
echo                   conda build and upload still run.
echo   --any-branch    Skip the requirement to be on the main branch.
echo.
echo Flags can be combined, e.g. --tag --conda-only.
echo Mutually exclusive: --pip-only and --conda-only.
echo.
echo Examples:
echo   release.bat                       full release (pip + conda)
echo   release.bat --tag                 auto-create tag, then full release
echo   release.bat --pip-only            pip only, to PyPI
echo   release.bat --pip-only --test     pip only, to TestPyPI
echo   release.bat --conda-only          conda only
echo   release.bat --skip-pip            build wheel (no upload), push conda
echo   release.bat --any-branch          release from a non-main branch
echo.
endlocal
exit /b 0

:fail
echo.
echo *** Release failed ***
endlocal
exit /b 1
