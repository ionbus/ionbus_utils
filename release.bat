@echo off
REM Build and publish ionbus-utils to PyPI and Anaconda.
REM Prereqs: activate an env that has: build, twine, conda-build, anaconda-client.
REM Auth: %USERPROFILE%\.pypirc for PyPI, `anaconda login` for Anaconda.
REM
REM Usage:
REM   release.bat            requires HEAD to already be tagged
REM   release.bat --tag      run auto_tag to create+push a new tag first
REM   release.bat --test     upload to TestPyPI instead of PyPI
REM   flags can be combined: release.bat --tag --test

setlocal enabledelayedexpansion

set "ANACONDA_USER=ionbus"
set "DO_TAG=0"
set "TEST_PYPI=0"

:parse_args
if "%~1"=="" goto after_args
if /i "%~1"=="--tag"  (set "DO_TAG=1" & shift & goto parse_args)
if /i "%~1"=="--test" (set "TEST_PYPI=1" & shift & goto parse_args)
echo Unknown arg: %~1 1>&2
exit /b 2
:after_args

cd /d "%~dp0"

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

echo === Building pip wheel ===
python -m build --wheel
if errorlevel 1 goto :fail

if "%TEST_PYPI%"=="1" (
    echo === Uploading to TestPyPI ===
    python -m twine upload --repository testpypi dist/*
) else (
    echo === Uploading to PyPI ===
    python -m twine upload dist/*
)
if errorlevel 1 goto :fail

echo === Resolving conda output path ===
for /f "delims=" %%i in ('conda build conda-recipe -c conda-forge --output') do set "CONDA_PKG=%%i"
echo Will build: !CONDA_PKG!

echo === Building conda package ===
conda build conda-recipe -c conda-forge
if errorlevel 1 goto :fail

echo === Uploading to Anaconda (user: %ANACONDA_USER%) ===
anaconda upload --user %ANACONDA_USER% "!CONDA_PKG!"
if errorlevel 1 goto :fail

echo === Done: released !TAG! ===
endlocal
exit /b 0

:fail
echo.
echo *** Release failed ***
endlocal
exit /b 1
