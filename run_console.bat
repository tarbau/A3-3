@echo off
REM Batch script to run console application on Windows
REM Double-click this file or run from command prompt

echo ============================================================
echo   Financial Data Analyzer - Console Application
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo.
    echo Please run these commands first:
    echo   python -m venv venv
    echo   venv\Scripts\activate.bat
    echo   pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if ticker provided as argument
if "%1"=="" (
    echo Running console application...
    echo.
    python -m app.console_app
) else (
    echo Running console application with ticker: %1
    echo.
    python -m app.console_app %1
)

echo.
pause

