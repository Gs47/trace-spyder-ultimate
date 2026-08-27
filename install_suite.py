import os, sys

print("[*] Trace Spyder Master Suite Installer initializing...")

# 1. MENU.PY GENERator
menu_code = r'''import os, sys, shutil, time, subprocess
import builtins

def safe_input(prompt=""):
    try: return _orig_input(prompt)
    except (EOFError, KeyboardInterrupt): sys.exit(0)
_orig_input = builtins.input
builtins.input = safe_input

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

MENU_ITEMS = {
    "1": ("Gmail Automation Bot", "gmail_bot.py"),
    "2": ("Telegram Hub Manager", "tg_manager.py"),
    "3": ("Universal Media Downloader", "media_dl.py"),
    "4": ("Spotify Music Downloader", "spotify_dl.py"),
    "5": ("TeraBox Cloud Downloader", "terabox_dl.py"),
    "6": ("Web Page & Asset DL", "web_dl.py"),
    "7": ("Audio/Video Converter", "converter.py"),
    "8": ("OSINT Target Recon", "recon_tool.py"),
    "9": ("Web Domain Recon", "web_recon.py"),
    "10": ("Network Audit & Scan", "net_tools.py"),
    "11": ("Seeker Location Engine", "seeker_hub.py"),
    "12": ("Phone Number Lookup", "check_number.py"),
    "13": ("AES Encrypted Vault", "file_vault.py"),
    "14": ("Cryptography & Ciphers", "crypto_tool.py"),
    "15": ("Hash Generator & Check", "hash_tool.py"),
    "16": ("Multi-Base Encoder", "encoder_tool.py"),
    "17": ("Secure Password Gen", "pwgen_tool.py"),
    "18": ("Disposable Temp Mail", "temp_mail.py"),
    "19": ("Link Unshortener", "link_unshort.py"),
    "20": ("Device Hardware Info", "device_info.py"),
    "21": ("Phone Storage Cleaner", "phone_cleaner.py"),
    "22": ("System Benchmark", "benchmark_tool.py"),
    "23": ("Zip Master Utility", "zip_master.py"),
    "24": ("QR Code Maker/Scan", "qr_tool.py"),
    "25": ("Terminal Quick Notes", "notes_tool.py"),
    "26": ("Multi-Engine Search", "search_engine.py"),
    "27": ("System Settings & Diagnostics", "settings.py"),
    "28": ("Complete Manual & About Us", "about.py")
}

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    bar = "─" * (w - 2)
    print(f"{C_CYAN}┌{bar}┐{C_RESET}")
    print(f"""{C_WHITE}  ████████╗██████╗  █████╗  ██████╗███████╗
  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
     ██║   ██████╔╝███████║██║     █████╗  
     ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
     ██║   ██║  ██║██║  ██║╚██████╗███████╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝

  ███████╗██████╗ ██╗   ██╗██████╗ ███████╗██████╗ 
  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
  ███████╗██████╔╝ ╚████╔╝ ██║  ██║█████╗  ██████╔╝
  ╚════██║██╔═══╝   ╚██╔╝  ██║  ██║██╔══╝  ██╔══██╗
  ███████║██║        ██║   ██████╔╝███████╗██║  ██║
  ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝{C_RESET}
         {C_YELLOW}🕷️  {C_CYAN}G O W R I   S H A N K A R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}TRACE SPYDER ULTIMATE{C_MAGENTA} ═ ⚡{C_RESET}""")
    print(f"{C_CYAN}└{bar}┘{C_RESET}")

def run_tool(filename):
    path = os.path.expanduser(f"~/{filename}")
    if os.path.exists(path):
        proc = subprocess.run([sys.executable, path])
        if proc.returncode == 99:
            print(f"\n{C_YELLOW}Exiting Trace Spyder Framework. Goodbye!{C_RESET}\n")
            sys.exit(0)
    else:
        print(f"\n{C_RED}❌ Error: '{filename}' not found.{C_RESET}")
        time.sleep(1)

def main():
    while True:
        w = get_screen_width()
        bar = "─" * (w - 2)
        print_banner()

        print(f"\n{C_YELLOW}╔{'═' * (w-2)}╗{C_RESET}")
        print(f"{C_YELLOW}║{C_RESET} {C_RED}[*]{C_GREEN} \033[1m🤖 TRACE SPYDER AI CHAT (NEURAL CORE) ⚡\033[0m {C_YELLOW}║{C_RESET}")
        print(f"{C_YELLOW}╚{'═' * (w-2)}╝{C_RESET}\n")

        for i in range(1, 29):
            k = str(i)
            name = MENU_ITEMS[k][0].upper()
            print(f"  {C_CYAN}[{i:02d}]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}\033[1m{name}\033[0m")

        print(f"\n{C_CYAN}┌{bar}┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}\033[1m[27] ⚙️  SYSTEM SETTINGS & DIAGNOSTICS\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_MAGENTA}\033[1m[28] 📖 COMPLETE MANUAL & ABOUT US\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_RED}\033[1m[0/x] 🚪 EXIT TERMINAL / CLOSE SESSION\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└{bar}┘{C_RESET}")

        raw = input(f"\n{C_GREEN}➤ Select Option ([*] AI / 1-28 / [0/x] Exit): {C_RESET}").strip().lower()

        if raw in ['*', '@', 'ai']:
            run_tool("ai_chat.py")
            continue

        if raw in ['0', '00', 'x', 'exit', 'q', 'quit']:
            print(f"\n{C_YELLOW}Closing Trace Spyder Terminal. Goodbye!{C_RESET}\n")
            sys.exit(0)

        choice_clean = raw.lstrip("0")
        if choice_clean in MENU_ITEMS:
            name, script = MENU_ITEMS[choice_clean]
            run_tool(script)

if __name__ == "__main__":
    main()
'''

with open(os.path.expanduser("~/menu.py"), "w") as f:
    f.write(menu_code)

# 2. SETUP.BAT FOR WINDOWS PC 1-CLICK LAUNCH
bat_code = r'''@echo off
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
'''

with open(os.path.expanduser("~/Setup.bat"), "w") as f:
    f.write(bat_code)

print("[+] Master menu.py and Setup.bat generated successfully!")
print("[+] You can now copy your home folder files or download the updated ZIP.")
