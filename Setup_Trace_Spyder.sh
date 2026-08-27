#!/data/data/com.termux/files/usr/bin/bash
clear

C_CYAN="\033[1;36m"
C_GREEN="\033[1;32m"
C_YELLOW="\033[1;33m"
C_RED="\033[1;31m"
C_RESET="\033[0m"

echo -e "${C_CYAN}┌────────────────────────────────────────────────────────────┐"
echo -e "         ${C_YELLOW}🕷️   G O W R I   S H A N K A R   🕷️${C_CYAN}"
echo -e "           ⚡ ═ UNIVERSAL AUTO-INSTALLER ═ ⚡"
echo -e "└────────────────────────────────────────────────────────────┘${C_RESET}"
echo ""
echo -e "${C_YELLOW}[?] Where are you installing Trace Spyder Terminal Hub?${C_RESET}"
echo -e "  ${C_CYAN}[1]${C_RESET} Android Mobile (Termux)"
echo -e "  ${C_CYAN}[2]${C_RESET} Windows Laptop / PC (Generate Auto-Setup Package)"
echo -e "${C_CYAN}─"*60 + "${C_RESET}"
read -p "➤ Choose Environment (1 or 2): " env_choice

if [ "$env_choice" == "1" ]; then
    echo -e "\n${C_YELLOW}[*] Configuring Android Termux environment...${C_RESET}"
    mkdir -p /data/data/com.termux/files/usr/tmp
    chmod 777 /data/data/com.termux/files/usr/tmp
    pkg update -y && pkg install python ffmpeg imagemagick poppler zip -y
    pip install requests yt-dlp spotdl telethon pillow
    
    # Shortcut alias
    if ! grep -q "alias gs=" ~/.bashrc 2>/dev/null; then
        echo "alias gs='python ~/menu.py'" >> ~/.bashrc
    fi
    echo -e "\n${C_GREEN}✅ Setup complete! Launching dashboard...${C_RESET}"
    python ~/menu.py

elif [ "$env_choice" == "2" ]; then
    echo -e "\n${C_YELLOW}[*] Creating Windows Laptop One-Click Auto-Installer...${C_RESET}"
    
    # Create Setup.bat for Windows
    cat << 'WINEOF' > ~/Setup.bat
@echo off
title Trace Spyder Hub - Windows Auto Installer
color 0b
cls

echo ============================================================
echo      TRACE SPYDER TERMINAL HUB - PC SETUP & LAUNCHER
echo ============================================================
echo.

:: Check & Install Python automatically
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Python not found! Installing Python via Winget...
    winget install Python.Python.3.11 --silent --accept-package-agreements --accept-source-agreements
    echo [✓] Python Installed!
) else (
    echo [✓] Python is detected.
)

:: Check & Install FFmpeg automatically
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] FFmpeg not found! Installing FFmpeg via Winget...
    winget install Gyan.FFmpeg --silent --accept-package-agreements --accept-source-agreements
    echo [✓] FFmpeg Installed!
) else (
    echo [✓] FFmpeg is detected.
)

:: Install required Python libraries
echo [*] Installing required Python dependencies...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install requests yt-dlp spotdl telethon pillow

echo.
echo ============================================================
echo [✓] SYSTEM READY! LAUNCHING TRACE SPYDER DASHBOARD...
echo ============================================================
timeout /t 2 >nul
cls
python menu.py
pause
WINEOF

    # Pack everything into Download/Trace_Spyder_PC.zip
    zip -r /sdcard/Download/Trace_Spyder_PC.zip ~/menu.py ~/tools.py ~/media_dl.py ~/spotify_dl.py ~/converter.py ~/temp_mail.py ~/device_info.py ~/phone_cleaner.py ~/seeker_hub.py ~/settings.py ~/auto_repair.py ~/Setup.bat
    
    echo -e "\n${C_GREEN}✅ Setup Package Successfully Created!${C_RESET}"
    echo -e "📂 Location: ${C_YELLOW}/sdcard/Download/Trace_Spyder_PC.zip${C_RESET}"
    echo -e "👉 Move this ZIP file to your laptop, extract it, and double-click 'Setup.bat'."
else
    echo -e "\n${C_RED}❌ Invalid selection!${C_RESET}"
fi
