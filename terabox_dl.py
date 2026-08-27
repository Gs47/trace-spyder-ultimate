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
    os.system('cls' if os.name=='nt' else 'clear')
    print(BANNER)
    print(f"\033[1;35m  [▸] ACTIVE MODULE : \033[1;32mTERABOX FAST DOWNLOADER\033[0m")
    print("\033[1;36m" + "─"*64 + "\033[0m")

def main():
    while True:
        clear_screen()
        url = input("\033[1;32m➤ Enter TeraBox Link ([#] Back / [*] Exit): \033[0m").strip()
        if url.lower() in ['#', 'b', 'back']: break
        elif url.lower() in ['*', 'x', 'exit', 'q']: os._exit(0)
        elif url:
            print(f"\n\033[1;33m[*] Connecting to stream server...\033[0m")
            subprocess.run(["yt-dlp", "-P", "/sdcard/Download", url])
            input("\n\033[1;32m[✓] Press Enter to continue...\033[0m")

if __name__ == "__main__": main()
