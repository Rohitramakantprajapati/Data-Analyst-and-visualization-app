@echo off
echo ========================================
echo  DataPro Analyst - Startup Script
echo ========================================
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo Python found!
echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo ========================================
echo Starting DataPro Analyst Server...
echo ========================================
echo.
echo The app will start on: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
timeout /t 3

python app.py

pause
