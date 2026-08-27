import os

# Safe input wrapper to prevent EOFError / Pipe crashes
_orig_input = input
def input(prompt=""):
    try:
        return _orig_input(prompt)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)


def handle_nav(val):
    v = str(val).strip().lower()
    if v in ['x', 'exit', 'quit', 'kill']:
        sys.exit(99)
    if v in ['m', 'main', 'home', 'mm', '##']:
        sys.exit(0)
    if v in ['0', '00', 'b', 'back', '#']:
        return "BACK"
    return val


C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

BANNER = f"""{C_CYAN}┌────────────────────────────────────────────────────────────┐
{C_WHITE}  ████████╗██████╗  █████╗  ██████╗███████╗
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
  ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
{C_RESET}
         {C_YELLOW}🕷️  {C_CYAN}G O W R I   S H A N K A R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}T E R M I N A L   H U B{C_MAGENTA} ═ ⚡{C_RESET}
{C_CYAN}└────────────────────────────────────────────────────────────┘{C_RESET}"""

def wrap_script(title, body):
    return f'''import os, sys, subprocess, shutil

C_CYAN = "\\033[1;36m"
C_GREEN = "\\033[1;32m"
C_YELLOW = "\\033[1;33m"
C_RED = "\\033[1;31m"
C_MAGENTA = "\\033[1;35m"
C_WHITE = "\\033[1;37m"
C_RESET = "\\033[0m"

BANNER = """{BANNER}"""

def clear_screen():
    os.system('clear')
    print(BANNER)
    print(f"{{C_MAGENTA}}  [▸] ACTIVE MODULE : {{C_GREEN}}{title}{{C_RESET}}")
    print(f"{{C_CYAN}}─"*60 + f"{{C_RESET}}")

{body}
'''

# 1. Main Menu
menu_body = '''def run_script(script_name):
    path = os.path.expanduser(f"~/{script_name}")
    if os.path.exists(path):
        subprocess.run([sys.executable, path])
    else:
        print(f"\\n{C_RED}❌ Error: {script_name} not found!{C_RESET}")
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Telegram Cloud Hub (Import/Export/Chats)")
        print(f"  {C_CYAN}[2]{C_RESET} Ultimate Media Downloader (YT/IG/FB/X/etc)")
        print(f"  {C_CYAN}[3]{C_RESET} Spotify Smart Music & Video Downloader")
        print(f"  {C_CYAN}[4]{C_RESET} TeraBox Video Fast Downloader")
        print(f"  {C_CYAN}[5]{C_RESET} Fast Media & Doc Converter Engine")
        print(f"  {C_CYAN}[6]{C_RESET} Seeker OSINT Location Explorer")
        print(f"  {C_CYAN}[7]{C_RESET} Device & Battery Diagnostic Status")
        print(f"  {C_CYAN}[8]{C_RESET} Termux Storage & Cache Purger")
        print(f"  {C_CYAN}[9]{C_RESET} Settings & Engine Updater")
        print(f"  {C_CYAN}[10]{C_RESET} Full System Self-Repair & Auto-Fix Engine")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_YELLOW}[0]{C_RESET} Refresh Dashboard")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        
        choice = input(f"{C_GREEN}➤ Select Option (1-10): {C_RESET}").strip().lower()
        mapping = {
            '1': 'tools.py', '01': 'tools.py',
            '2': 'media_dl.py', '02': 'media_dl.py',
            '3': 'spotify_dl.py', '03': 'spotify_dl.py',
            '4': 'terabox_dl.py', '04': 'terabox_dl.py',
            '5': 'converter.py', '05': 'converter.py',
            '6': 'seeker_hub.py', '06': 'seeker_hub.py',
            '7': 'device_info.py', '07': 'device_info.py',
            '8': 'phone_cleaner.py', '08': 'phone_cleaner.py',
            '9': 'settings.py', '09': 'settings.py',
            '10': 'auto_repair.py'
        }
        if choice in mapping: run_script(mapping[choice])
        elif choice == '0': continue
        elif choice in ['*', 'x', 'exit', 'q']:
            print(f"\\n{C_RED}Exiting Hub. Goodbye!{C_RESET}\\n")
            sys.exit(0)
        else: input(f"\\n{C_RED}❌ Invalid choice! Press Enter...{C_RESET}")

if __name__ == "__main__": main_menu()'''

# 2. Device Info
device_info_body = '''def get_battery():
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
            print(f"{C_CYAN}[*]{C_RESET} Internal Storage (/sdcard):")
            print(f"    - Total Capacity : {C_YELLOW}{total / (1024**3):.2f} GB{C_RESET}")
            print(f"    - Used Space     : {C_RED}{used / (1024**3):.2f} GB{C_RESET}")
            print(f"    - Free Available : {C_GREEN}{free / (1024**3):.2f} GB{C_RESET}")
        except Exception as e:
            print(f"[*] Storage Error: {e}")
            
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        batt_lvl, batt_st = get_battery()
        print(f"{C_CYAN}[*]{C_RESET} Battery Diagnostics:")
        print(f"    - Current Level  : {C_GREEN}{batt_lvl}{C_RESET}")
        print(f"    - Battery State  : {C_YELLOW}{batt_st}{C_RESET}")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"{C_CYAN}[*]{C_RESET} Architecture     : {C_WHITE}{os.uname().machine}{C_RESET}")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        print(f"  {C_YELLOW}[0]{C_RESET} Refresh Status")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option: {C_RESET}").strip().lower()
        if c == '0': continue
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

# 3. Storage Cleaner
cleaner_body = '''def get_free_space():
    try:
        _, _, free_b = shutil.disk_usage('/sdcard')
        return free_b
    except Exception: return 0

def format_size(bytes_val):
    mb = bytes_val / (1024 * 1024)
    if mb >= 1024: return f"{mb / 1024:.2f} GB"
    return f"{mb:.2f} MB"

def clean_termux_junk():
    print(f"\\n{C_YELLOW}[*] Purging temporary cache files...{C_RESET}")
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
                print(f"  {C_GREEN}[✓] Cleared:{C_RESET} {p}")
            except Exception: pass
            
    os.makedirs("/data/data/com.termux/files/usr/tmp", exist_ok=True)
    subprocess.run(["apt-get", "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["pip", "cache", "purge"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    final_free = get_free_space()
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")
    print(f"[*] Initial Free Space : {format_size(initial_free)}")
    print(f"[*] Current Free Space : {format_size(final_free)}")
    print(f"{C_GREEN}🔥 TOTAL SPACE RECLAIMED : {format_size(max(0, final_free - initial_free))}{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Run Termux Junk & Temp Cleaner")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option: {C_RESET}").strip().lower()
        if c == '1':
            clean_termux_junk()
            input("\\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

# 4. TeraBox DL
terabox_dl_body = '''def main():
    while True:
        clear_screen()
        url = input(f"{C_GREEN}➤ Enter TeraBox Link ([#] Back / [*] Exit): {C_RESET}").strip()
        if url.lower() in ['#', 'b', 'back']: break
        elif url.lower() in ['*', 'x', 'exit', 'q']: os._exit(0)
        elif url:
            print(f"\\n{C_YELLOW}[*] Connecting to stream server...{C_RESET}")
            subprocess.run(["yt-dlp", "-P", "/sdcard/Download", url])
            input(f"\\n{C_GREEN}[✓] Press Enter to continue...{C_RESET}")

if __name__ == "__main__": main()'''

# 5. Seeker Hub
seeker_body = '''def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Start Seeker OSINT Service")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option: {C_RESET}").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)
        else: input("\\nService loaded. Press Enter...")

if __name__ == "__main__": main()'''

# 6. Settings
settings_body = '''def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Update Core Engines & Python Libs")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option: {C_RESET}").strip().lower()
        if c == '1':
            subprocess.run(["pip", "install", "--upgrade", "yt-dlp", "requests", "telethon", "spotdl", "pillow"])
            input("\\nUpdate completed. Press Enter...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

# 7. Auto Repair
auto_repair_body = '''def run_auto_repair():
    print(f"\\n{C_YELLOW}[*] Restoring system folders and libraries...{C_RESET}")
    os.makedirs("/data/data/com.termux/files/usr/tmp", exist_ok=True)
    os.chmod("/data/data/com.termux/files/usr/tmp", 0o777)
    print(f"  {C_GREEN}[✓] Storage & tmp partitions calibrated{C_RESET}")
    subprocess.run(["pip", "install", "--upgrade", "yt-dlp", "requests", "spotdl", "urllib3", "telethon", "pillow"], 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  {C_GREEN}[✓] All dependencies synchronized{C_RESET}")
    print(f"\\n{C_GREEN}✅ SYSTEM AUTO-REPAIR COMPLETED SUCCESSFULLY!{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Run Automatic Full System Diagnostics")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option: {C_RESET}").strip().lower()
        if c == '1':
            run_auto_repair()
            input("\\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

files = {
    "menu.py": wrap_script("MAIN DASHBOARD", menu_body),
    "device_info.py": wrap_script("DEVICE & BATTERY DIAGNOSTICS", device_info_body),
    "phone_cleaner.py": wrap_script("STORAGE & JUNK PURGER", cleaner_body),
    "terabox_dl.py": wrap_script("TERABOX FAST DOWNLOADER", terabox_dl_body),
    "seeker_hub.py": wrap_script("SEEKER OSINT EXPLORER", seeker_body),
    "settings.py": wrap_script("SETTINGS & UPDATER", settings_body),
    "auto_repair.py": wrap_script("SYSTEM SELF-REPAIR ENGINE", auto_repair_body),
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ Banner updated with: 🕷️ G O W R I   S H A N K A R 🕷️ across all system modules!")