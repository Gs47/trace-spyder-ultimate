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
    print(f"\033[1;35m  [▸] ACTIVE MODULE : \033[1;32mMEDIA CONVERTER ENGINE\033[0m")
    print("\033[1;36m" + "─"*64 + "\033[0m")

def main():
    while True:
        clear_screen()
        print("  \033[1;33m[1]\033[0m Convert Video to MP3 Audio (320kbps)")
        print("\033[1;36m" + "─"*64 + "\033[0m")
        print("  \033[1;36m[#]\033[0m Back to Main Menu")
        print("  \033[1;31m[*]\033[0m Full Exit to Terminal")
        print("\033[1;36m" + "═"*64 + "\033[0m")
        c = input("\033[1;32m➤ Option: \033[0m").strip().lower()
        if c == '1':
            v_path = input("Enter Full Video File Path: ").strip()
            if os.path.exists(v_path):
                out = v_path.rsplit(".", 1)[0] + ".mp3"
                subprocess.run(["ffmpeg", "-i", v_path, "-vn", "-ab", "320k", out])
                print(f"\n\033[1;32m[✓] Converted Output: {out}\033[0m")
            else:
                print("\033[1;31m❌ File path not found.\033[0m")
            input("\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()
