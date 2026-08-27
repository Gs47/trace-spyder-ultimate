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
    print(f"\033[1;35m  [▸] ACTIVE MODULE : \033[1;32mDEVICE & BATTERY DIAGNOSTICS\033[0m")
    print("\033[1;36m" + "─"*64 + "\033[0m")

def get_battery():
    paths = {
        "level": ["/sys/class/power_supply/battery/capacity", "/sys/class/power_supply/bms/capacity"],
        "status": ["/sys/class/power_supply/battery/status", "/sys/class/power_supply/battery/charging_enabled"]
    }
    lvl, st = "N/A", "Discharging / Idle"
    for p in paths["level"]:
        if os.path.exists(p):
            try:
                with open(p, 'r') as f: lvl = f.read().strip() + "%"; break
            except Exception: pass
    for p in paths["status"]:
        if os.path.exists(p):
            try:
                with open(p, 'r') as f: st = f.read().strip(); break
            except Exception: pass
    return lvl, st

def main():
    while True:
        clear_screen()
        try:
            total, used, free = shutil.disk_usage('/sdcard')
            print(f"[*] Internal Storage (/sdcard):")
            print(f"    - Total Capacity : \033[1;33m{total / (1024**3):.2f} GB\033[0m")
            print(f"    - Used Space     : \033[1;31m{used / (1024**3):.2f} GB\033[0m")
            print(f"    - Free Available : \033[1;32m{free / (1024**3):.2f} GB\033[0m")
        except Exception as e:
            print(f"[*] Storage Error: {e}")
            
        print("─" * 64)
        batt_lvl, batt_st = get_battery()
        print(f"[*] Battery Diagnostics:")
        print(f"    - Current Level  : \033[1;32m{batt_lvl}\033[0m")
        print(f"    - Battery State  : \033[1;33m{batt_st}\033[0m")
        print("─" * 64)
        print(f"[*] Architecture     : {os.uname().machine}")
        print("\033[1;36m" + "─"*64 + "\033[0m")
        print("  \033[1;33m[0]\033[0m Refresh Status")
        print("  \033[1;36m[#]\033[0m Back to Main Menu")
        print("  \033[1;31m[*]\033[0m Full Exit to Terminal")
        print("\033[1;36m" + "═"*64 + "\033[0m")
        c = input("\033[1;32m➤ Option: \033[0m").strip().lower()
        if c == '0': continue
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()
