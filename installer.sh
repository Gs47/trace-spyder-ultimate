#!/data/data/com.termux/files/usr/bin/bash
clear

C_CYAN="\033[1;36m"
C_GREEN="\033[1;32m"
C_YELLOW="\033[1;33m"
C_RED="\033[1;31m"
C_MAGENTA="\033[1;35m"
C_RESET="\033[0m"

echo -e "${C_CYAN}┌──────────────────────────────────────────────┐"
echo -e "   ${C_YELLOW}🕷️  GOWRISANKAR B - TERMINAL HUB  🕷️${C_CYAN}"
echo -e "     ${C_MAGENTA}⚡ UNIVERSAL PLATFORM INSTALLER ⚡${C_CYAN}"
echo -e "└──────────────────────────────────────────────┘${C_RESET}"
echo ""
echo -e "${C_YELLOW}[?] Where are you installing Trace Spyder?${C_RESET}"
echo -e "  ${C_CYAN}[1]${C_RESET} Android Device (Termux Environment)"
echo -e "  ${C_CYAN}[2]${C_RESET} Windows Laptop / PC (Generate PC Package)"
echo -e "${C_CYAN}────────────────────────────────────────────────${C_RESET}"
read -p "➤ Select Platform (1 or 2): " plat_choice

if [ "$plat_choice" == "1" ]; then
    echo -e "\n${C_YELLOW}[*] Configuring Android Mobile Environment...${C_RESET}"
    mkdir -p /data/data/com.termux/files/usr/tmp
    chmod 777 /data/data/com.termux/files/usr/tmp
    pkg update -y && pkg install python ffmpeg imagemagick poppler zip -y
    pip install requests yt-dlp spotdl telethon pillow qrcode cryptography speedtest-cli
    
    # Shortcut 'gs'
    if ! grep -q "alias gs=" ~/.bashrc 2>/dev/null; then
        echo "alias gs='python ~/menu.py'" >> ~/.bashrc
    fi
    echo -e "\n${C_GREEN}✅ Android Setup Complete! Launching Dashboard...${C_RESET}"
    python ~/menu.py

elif [ "$plat_choice" == "2" ]; then
    echo -e "\n${C_YELLOW}[*] Packaging 100% Cross-Platform Files for PC...${C_RESET}"
    zip -r /sdcard/Download/Trace_Spyder_Ultimate_PC.zip ~/menu.py ~/tools.py ~/media_dl.py ~/spotify_dl.py ~/converter.py ~/temp_mail.py ~/zip_master.py ~/net_tools.py ~/qr_tool.py ~/file_vault.py ~/link_unshort.py ~/device_info.py ~/phone_cleaner.py ~/seeker_hub.py ~/settings.py ~/auto_repair.py ~/about.py ~/recon_tool.py ~/crypto_tool.py ~/benchmark_tool.py ~/hash_tool.py ~/encoder_tool.py ~/pwgen_tool.py ~/web_recon.py ~/notes_tool.py ~/Setup.bat
    
    echo -e "\n${C_GREEN}✅ Windows Setup Package Generated Successfully!${C_RESET}"
    echo -e "📂 Location: ${C_YELLOW}/sdcard/Download/Trace_Spyder_Ultimate_PC.zip${C_RESET}"
    echo -e "👉 Move this ZIP to your Laptop, extract it, and run 'Setup.bat'."
else
    echo -e "\n${C_RED}❌ Invalid selection! Exiting.${C_RESET}"
fi
