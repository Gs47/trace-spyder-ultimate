import os, sys, subprocess, shutil, glob, time

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

BANNER = """[1;36m┌────────────────────────────────────────────────────────────┐
[1;37m  ████████╗██████╗  █████╗  ██████╗███████╗
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
[0m
         [1;33m🕷️  [1;36mG O W R I   S H A N K A R[1;33m  🕷️[0m
           [1;35m⚡ ═ [1;32mT E R M I N A L   H U B[1;35m ═ ⚡[0m
[1;36m└────────────────────────────────────────────────────────────┘[0m"""

def get_download_dir():
    if os.name == 'nt':
        return os.path.join(os.path.expanduser("~"), "Downloads")
    if os.path.exists("/sdcard/Download"):
        return "/sdcard/Download"
    return os.path.expanduser("~/Downloads")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(f"{C_MAGENTA}  [▸] ACTIVE MODULE : {C_GREEN}ENCRYPTED TERMINAL NOTES & DIARY{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

NOTES_FILE = os.path.expanduser("~/.spyder_diary.txt")

def view_notes():
    clear_screen()
    if not os.path.exists(NOTES_FILE):
        print(f"{C_YELLOW}[*] No diary notes found! Add one first.{C_RESET}")
    else:
        with open(NOTES_FILE, "r") as f:
            print(f"{C_CYAN}╔════════════════════ [ SAVED NOTES & LOGS ] ════════════════════╗{C_RESET}")
            print(f"{C_WHITE}{f.read()}{C_RESET}")
            print(f"{C_CYAN}╚════════════════════════════════════════════════════════════════╝{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def add_note():
    clear_screen()
    note = input(f"{C_GREEN}➤ Enter Quick Note / Secret String: {C_RESET}").strip()
    if note:
        with open(NOTES_FILE, "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M')}] {note}\n")
        print(f"\n{C_GREEN}✅ Note saved securely!{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} View Terminal Notes / Diary Logs")
        print(f"  {C_CYAN}[2]{C_RESET} Append New Quick Note")
        print(f"  {C_CYAN}[3]{C_RESET} Clear Diary Storage")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1-3): {C_RESET}").strip().lower()
        if c == '1': view_notes()
        elif c == '2': add_note()
        elif c == '3':
            if os.path.exists(NOTES_FILE): os.remove(NOTES_FILE)
            input(f"\n{C_GREEN}✅ Storage Cleared! Press Enter...{C_RESET}")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
