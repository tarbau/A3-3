@echo off
REM Batch script to run web dashboard on Windows
REM Double-click this file or run from command prompt

echo ============================================================
echo   Financial Data Analyzer - Web Dashboard
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

echo Starting web server...
echo.
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python -m app.web_app

pause

