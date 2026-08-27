@echo off
TITLE TRACE SPYDER ULTIMATE SUITE - GOWRI SHANKAR
color 0b
echo ========================================================
echo    TRACE SPYDER TERMINAL SUITE - INITIALIZING...
echo ========================================================
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or added to PATH! Please install Python.
    pause
    exit /b
)
python -m pip install --upgrade requests yt-dlp beautifulsoup4 --quiet
cls
python menu.py
pause
