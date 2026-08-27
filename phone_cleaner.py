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
    print(f"\033[1;35m  [▸] ACTIVE MODULE : \033[1;32mSTORAGE & JUNK PURGER\033[0m")
    print("\033[1;36m" + "─"*64 + "\033[0m")

def get_free_space():
    try:
        _, _, free_b = shutil.disk_usage('/sdcard')
        return free_b
    except Exception: return 0

def format_size(bytes_val):
    mb = bytes_val / (1024 * 1024)
    if mb >= 1024: return f"{mb / 1024:.2f} GB"
    return f"{mb:.2f} MB"

def clean_termux_junk():
    print("\n\033[1;33m[*] Purging temporary cache files...\033[0m")
    initial_free = get_free_space()
    paths = [
        "/data/data/com.termux/files/usr/tmp",
        os.path.expanduser("~/.cache"),
        os.path.expanduser("~/.npm"),
        os.path.expanduser("~/.pip")
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                if os.path.isdir(p): shutil.rmtree(p, ignore_errors=True)
                else: os.remove(p)
                print(f"  \033[1;32m[✓] Cleared:\033[0m {p}")
            except Exception: pass
            
    os.makedirs("/data/data/com.termux/files/usr/tmp", exist_ok=True)
    subprocess.run(["apt-get", "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["pip", "cache", "purge"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    final_free = get_free_space()
    print("─" * 64)
    print(f"[*] Initial Free Space : {format_size(initial_free)}")
    print(f"[*] Current Free Space : {format_size(final_free)}")
    print(f"\033[1;32m🔥 TOTAL SPACE RECLAIMED : {format_size(max(0, final_free - initial_free))}\033[0m")
    print("─" * 64)

def main():
    while True:
        clear_screen()
        print("  \033[1;33m[1]\033[0m Run Termux Junk & Temp Cleaner")
        print("\033[1;36m" + "─"*64 + "\033[0m")
        print("  \033[1;36m[#]\033[0m Back to Main Menu")
        print("  \033[1;31m[*]\033[0m Full Exit to Terminal")
        print("\033[1;36m" + "═"*64 + "\033[0m")
        c = input("\033[1;32m➤ Option: \033[0m").strip().lower()
        if c == '1':
            clean_termux_junk()
            input("\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()
