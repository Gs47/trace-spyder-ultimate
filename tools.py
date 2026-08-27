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
    print(f"\033[1;35m  [▸] ACTIVE MODULE : \033[1;32mTELEGRAM BOT & TOOLS\033[0m")
    print("\033[1;36m" + "─"*64 + "\033[0m")

def main():
    while True:
        clear_screen()
        print("  \033[1;33m[1]\033[0m Telegram Session String Generator")
        print("\033[1;36m" + "─"*64 + "\033[0m")
        print("  \033[1;36m[#]\033[0m Back to Main Menu")
        print("  \033[1;31m[*]\033[0m Full Exit to Terminal")
        print("\033[1;36m" + "═"*64 + "\033[0m")
        c = input("\033[1;32m➤ Option: \033[0m").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)
        else: input("\nModule ready. Press Enter...")

if __name__ == "__main__": main()
