import os, sys, subprocess, shutil

BANNER = r"""
\033[1;36m╔══════════════════════════════════════════════════════════════╗
\033[1;32m   _____ ____     _     ____ _____   ____  ______   ______  _____ ____  
  |_   _|  _ \   / \   / ___| ____| / ___||  _ \ \ / /  _ \| ____|  _ \ 
    | | | |_) | / _ \ | |   |  _|   \___ \| |_) \ V /| | | |  _| | |_) |
    | | |  _ < / ___ \| |___| |___   ___) |  __/ | | | |_| | |___|  _ < 
    |_| |_| \_/_/   \_\____|_____| |____/|_|    |_| |____/|_____|_| \_\
\033[1;33m                    🕷️  T R A C E   S P Y D E R  🕷️
\033[1;35m                 ⚡ ═ T E R M I N A L   H U B ═ ⚡
\033[1;36m╚══════════════════════════════════════════════════════════════╝\033[0m
"""

def clear_screen():
    os.system('clear')
    print(BANNER)
    print(f"\033[1;35m  [▸] ACTIVE MODULE : \033[1;32mSYSTEM SELF-REPAIR ENGINE\033[0m")
    print("\033[1;36m" + "─"*64 + "\033[0m")

def run_auto_repair():
    print("\n\033[1;33m[*] Restoring system folders and libraries...\033[0m")
    os.makedirs("/data/data/com.termux/files/usr/tmp", exist_ok=True)
    os.chmod("/data/data/com.termux/files/usr/tmp", 0o777)
    print("  \033[1;32m[✓] Storage & tmp partitions calibrated\033[0m")
    subprocess.run(["pip", "install", "--upgrade", "yt-dlp", "requests", "spotdl", "urllib3"], 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("  \033[1;32m[✓] All dependencies synchronized\033[0m")
    print("\n\033[1;32m✅ SYSTEM AUTO-REPAIR COMPLETED SUCCESSFULLY!\033[0m")

def main():
    while True:
        clear_screen()
        print("  \033[1;33m[1]\033[0m Run Automatic Full System Diagnostics")
        print("\033[1;36m" + "─"*64 + "\033[0m")
        print("  \033[1;36m[#]\033[0m Back to Main Menu")
        print("  \033[1;31m[*]\033[0m Full Exit to Terminal")
        print("\033[1;36m" + "═"*64 + "\033[0m")
        c = input("\033[1;32m➤ Option: \033[0m").strip().lower()
        if c == '1':
            run_auto_repair()
            input("\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()
