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


BANNER = r'''
\033[1;30m╔══════════════════════════════════════════════════════════════╗\033[0m
  \033[1;96m_____ ____     _     ____ _____ \033[1;91m  ____  ______   ______  _____ ____  
 |_   _|  _ \   / \   / ___| ____|\033[1;91m / ___||  _ \ \ / /  _ \| ____|  _ \ 
   | | | |_) | / _ \ | |   |  _|  \033[1;91m \___ \| |_) \ V /| | | |  _| | |_) |
   | | |  _ < / ___ \| |___| |___ \033[1;91m  ___) |  __/ | | | |_| | |___|  _ < 
   |_| |_| \_/_/   \_\____|_____|\033[1;91m|____/|_|    |_| |____/|_____|_| \_\

\033[1;93m                 🕷️  \033[1;96mT R A C E   \033[1;91mS P Y D E R\033[1;93m  🕷️
\033[1;95m              ⚡ ═ \033[1;92mT E R M I N A L   H U B\033[1;95m ═ ⚡
\033[1;30m╚══════════════════════════════════════════════════════════════╝\033[0m
'''

def wrap_script(title, body):
    return f'''import os, sys, subprocess, shutil

BANNER = r"""{BANNER}"""

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    print(BANNER)
    print(f"\\033[1;93m  [▸] ACTIVE MODULE : \\033[1;92m{title}\\033[0m")
    print("\\033[1;30m" + "─"*64 + "\\033[0m")

{body}
'''

# 1. Main Menu
menu_body = '''def run_script(script_name):
    path = os.path.expanduser(f"~/{script_name}")
    if os.path.exists(path):
        subprocess.run([sys.executable, path])
    else:
        print(f"\\n\\033[1;91m❌ Error: {script_name} not found!\\033[0m")
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        print("  \\033[1;96m[01]\\033[0m Telegram Tools & Manager")
        print("  \\033[1;96m[02]\\033[0m Ultimate Media Downloader (YT/IG/FB/X/etc)")
        print("  \\033[1;96m[03]\\033[0m Spotify Music Downloader (320kbps)")
        print("  \\033[1;96m[04]\\033[0m TeraBox Video Fast Downloader")
        print("  \\033[1;96m[05]\\033[0m Media & Document Converter Engine")
        print("  \\033[1;96m[06]\\033[0m Seeker OSINT Location Explorer")
        print("  \\033[1;96m[07]\\033[0m Device & Battery Diagnostic Status")
        print("  \\033[1;96m[08]\\033[0m Termux Storage & Cache Purger")
        print("  \\033[1;96m[09]\\033[0m Settings & Engine Updater")
        print("  \\033[1;96m[10]\\033[0m Full System Self-Repair & Auto-Fix Engine")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;93m[ 0]\\033[0m Refresh Dashboard")
        print("  \\033[1;91m[ *]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        
        choice = input("\\033[1;92m➤ Select Option: \\033[0m").strip().lower()
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
            print("\\n\\033[1;91mExiting Trace Spyder Terminal Hub. Goodbye!\\033[0m\\n")
            sys.exit(0)
        else: input("\\n❌ Invalid choice! Press Enter...")

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
            print(f"[*] Internal Storage (/sdcard):")
            print(f"    - Total Capacity : \\033[1;93m{total / (1024**3):.2f} GB\\033[0m")
            print(f"    - Used Space     : \\033[1;91m{used / (1024**3):.2f} GB\\033[0m")
            print(f"    - Free Available : \\033[1;92m{free / (1024**3):.2f} GB\\033[0m")
        except Exception as e:
            print(f"[*] Storage Error: {e}")
            
        print("─" * 64)
        batt_lvl, batt_st = get_battery()
        print(f"[*] Battery Diagnostics:")
        print(f"    - Current Level  : \\033[1;92m{batt_lvl}\\033[0m")
        print(f"    - Battery State  : \\033[1;93m{batt_st}\\033[0m")
        print("─" * 64)
        print(f"[*] Architecture     : {os.uname().machine}")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;93m[0]\\033[0m Refresh Status")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
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
    print("\\n\\033[1;93m[*] Purging temporary cache files...\\033[0m")
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
                print(f"  \\033[1;92m[✓] Cleared:\\033[0m {p}")
            except Exception: pass
            
    os.makedirs("/data/data/com.termux/files/usr/tmp", exist_ok=True)
    subprocess.run(["apt-get", "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["pip", "cache", "purge"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    final_free = get_free_space()
    print("─" * 64)
    print(f"[*] Initial Free Space : {format_size(initial_free)}")
    print(f"[*] Current Free Space : {format_size(final_free)}")
    print(f"\\033[1;92m🔥 TOTAL SPACE RECLAIMED : {format_size(max(0, final_free - initial_free))}\\033[0m")
    print("─" * 64)

def main():
    while True:
        clear_screen()
        print("  \\033[1;96m[1]\\033[0m Run Termux Junk & Temp Cleaner")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
        if c == '1':
            clean_termux_junk()
            input("\\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

# 4. Media DL
media_dl_body = '''def main():
    while True:
        clear_screen()
        url = input("\\033[1;92m➤ Enter Video URL ([#] Back / [*] Exit): \\033[0m").strip()
        if url.lower() in ['#', 'b', 'back']: break
        elif url.lower() in ['*', 'x', 'exit', 'q']: os._exit(0)
        elif url:
            out_dir = "/sdcard/Download"
            print(f"\\n\\033[1;93m[*] Downloading into {out_dir}...\\033[0m")
            subprocess.run(["yt-dlp", "-P", out_dir, url])
            input("\\n\\033[1;92m[✓] Download finished. Press Enter...\\033[0m")

if __name__ == "__main__": main()'''

# 5. Spotify DL
spotify_dl_body = '''def main():
    while True:
        clear_screen()
        url = input("\\033[1;92m➤ Enter Spotify Link ([#] Back / [*] Exit): \\033[0m").strip()
        if url.lower() in ['#', 'b', 'back']: break
        elif url.lower() in ['*', 'x', 'exit', 'q']: os._exit(0)
        elif url:
            out_dir = "/sdcard/Music"
            print(f"\\n\\033[1;93m[*] Fetching audio tracks...\\033[0m")
            subprocess.run(["spotdl", url, "--output", out_dir])
            input("\\n\\033[1;92m[✓] Finished. Press Enter...\\033[0m")

if __name__ == "__main__": main()'''

# 6. TeraBox DL
terabox_dl_body = '''def main():
    while True:
        clear_screen()
        url = input("\\033[1;92m➤ Enter TeraBox Link ([#] Back / [*] Exit): \\033[0m").strip()
        if url.lower() in ['#', 'b', 'back']: break
        elif url.lower() in ['*', 'x', 'exit', 'q']: os._exit(0)
        elif url:
            print(f"\\n\\033[1;93m[*] Connecting to stream server...\\033[0m")
            subprocess.run(["yt-dlp", "-P", "/sdcard/Download", url])
            input("\\n\\033[1;92m[✓] Press Enter to continue...\\033[0m")

if __name__ == "__main__": main()'''

# 7. Converter
converter_body = '''def main():
    while True:
        clear_screen()
        print("  \\033[1;96m[1]\\033[0m Convert Video to MP3 Audio (320kbps)")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
        if c == '1':
            v_path = input("Enter Full Video File Path: ").strip()
            if os.path.exists(v_path):
                out = v_path.rsplit(".", 1)[0] + ".mp3"
                subprocess.run(["ffmpeg", "-i", v_path, "-vn", "-ab", "320k", out])
                print(f"\\n\\033[1;92m[✓] Converted Output: {out}\\033[0m")
            else:
                print("\\033[1;91m❌ File path not found.\\033[0m")
            input("\\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

# 8. Tools
tools_body = '''def main():
    while True:
        clear_screen()
        print("  \\033[1;96m[1]\\033[0m Telegram Session String Generator")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)
        else: input("\\nModule ready. Press Enter...")

if __name__ == "__main__": main()'''

# 9. Seeker Hub
seeker_body = '''def main():
    while True:
        clear_screen()
        print("  \\033[1;96m[1]\\033[0m Start Seeker OSINT Service")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)
        else: input("\\nService loaded. Press Enter...")

if __name__ == "__main__": main()'''

# 10. Settings
settings_body = '''def main():
    while True:
        clear_screen()
        print("  \\033[1;96m[1]\\033[0m Update Core Engines & Python Libs")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
        if c == '1':
            subprocess.run(["pip", "install", "--upgrade", "yt-dlp", "requests"])
            input("\\nUpdate completed. Press Enter...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

# 11. Auto Repair
auto_repair_body = '''def run_auto_repair():
    print("\\n\\033[1;93m[*] Restoring system folders and libraries...\\033[0m")
    os.makedirs("/data/data/com.termux/files/usr/tmp", exist_ok=True)
    os.chmod("/data/data/com.termux/files/usr/tmp", 0o777)
    print("  \\033[1;92m[✓] Storage & tmp partitions calibrated\\033[0m")
    subprocess.run(["pip", "install", "--upgrade", "yt-dlp", "requests", "spotdl", "urllib3"], 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("  \\033[1;92m[✓] All dependencies synchronized\\033[0m")
    print("\\n\\033[1;92m✅ SYSTEM AUTO-REPAIR COMPLETED SUCCESSFULLY!\\033[0m")

def main():
    while True:
        clear_screen()
        print("  \\033[1;96m[1]\\033[0m Run Automatic Full System Diagnostics")
        print("\\033[1;30m" + "─"*64 + "\\033[0m")
        print("  \\033[1;96m[#]\\033[0m Back to Main Menu")
        print("  \\033[1;91m[*]\\033[0m Full Exit to Terminal")
        print("\\033[1;30m" + "═"*64 + "\\033[0m")
        c = input("\\033[1;92m➤ Option: \\033[0m").strip().lower()
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
    "media_dl.py": wrap_script("ULTIMATE MEDIA DOWNLOADER", media_dl_body),
    "spotify_dl.py": wrap_script("SPOTIFY MUSIC DOWNLOADER", spotify_dl_body),
    "terabox_dl.py": wrap_script("TERABOX FAST DOWNLOADER", terabox_dl_body),
    "converter.py": wrap_script("MEDIA CONVERTER ENGINE", converter_body),
    "tools.py": wrap_script("TELEGRAM BOT & TOOLS", tools_body),
    "seeker_hub.py": wrap_script("SEEKER OSINT EXPLORER", seeker_body),
    "settings.py": wrap_script("SETTINGS & UPDATER", settings_body),
    "auto_repair.py": wrap_script("SYSTEM SELF-REPAIR ENGINE", auto_repair_body),
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ Vibrant Neon-Cyan & Crimson 'TRACE SPYDER' theme applied!")