import os, sys, subprocess, shutil, glob

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

def get_music_dir():
    if os.name == 'nt':
        return os.path.join(os.path.expanduser("~"), "Music")
    if os.path.exists("/sdcard/Music"):
        return "/sdcard/Music"
    return os.path.expanduser("~/Music")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(f"{C_MAGENTA}  [▸] ACTIVE MODULE : {C_GREEN}ARCHIVE & ZIP MASTER ENGINE{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

import zipfile, itertools, string

def get_input_path(prompt_text):
    path = input(f"{C_GREEN}➤ {prompt_text} ([#] Back / [*] Exit): {C_RESET}").strip().strip("'\"")
    if path.lower() in ['#', 'b', 'back']: return None
    elif path.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
    if not os.path.exists(path):
        print(f"\n{C_RED}❌ Error: Path not found!{C_RESET}")
        input("Press Enter...")
        return False
    return path

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Create ZIP File (Compress Folder / Files)")
        print(f"  {C_CYAN}[2]{C_RESET} Extract Normal ZIP Archive (Standard Unzip)")
        print(f"  {C_CYAN}[3]{C_RESET} Unlock / Recover Password-Protected ZIP")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        c = input(f"{C_GREEN}➤ Select Option (1-3): {C_RESET}").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)
        elif c == '1':
            target = get_input_path("Enter Folder/File to ZIP")
            if target:
                out_zip = target.rstrip("/\\") + ".zip"
                with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as z:
                    if os.path.isdir(target):
                        for root, _, files in os.walk(target):
                            for f in files:
                                fp = os.path.join(root, f)
                                z.write(fp, os.path.relpath(fp, os.path.dirname(target)))
                    else: z.write(target, os.path.basename(target))
                input(f"\n{C_GREEN}✅ Created: {out_zip}! Press Enter...{C_RESET}")
        elif c == '2':
            zp = get_input_path("Enter .zip File Path")
            if zp:
                od = os.path.splitext(zp)[0] + "_extracted"
                os.makedirs(od, exist_ok=True)
                pwd = input("Password (leave blank if none): ").strip()
                try:
                    with zipfile.ZipFile(zp, 'r') as z: z.extractall(od, pwd=pwd.encode() if pwd else None)
                    input(f"\n{C_GREEN}✅ Extracted to {od}! Press Enter...{C_RESET}")
                except Exception as e: input(f"\n{C_RED}❌ Error: {e}. Press Enter...{C_RESET}")
        elif c == '3':
            zp = get_input_path("Enter Protected .zip File Path")
            if zp:
                od = os.path.splitext(zp)[0] + "_unlocked"
                os.makedirs(od, exist_ok=True)
                max_l = input("Max length to brute-force (e.g. 4): ").strip()
                max_l = int(max_l) if max_l.isdigit() else 4
                zf = zipfile.ZipFile(zp)
                found = None
                for l in range(1, max_l + 1):
                    if found: break
                    for att in itertools.product(string.digits + string.ascii_lowercase, repeat=l):
                        w = ''.join(att)
                        try:
                            zf.extractall(od, pwd=w.encode())
                            found = w
                            break
                        except Exception: continue
                if found: input(f"\n{C_GREEN}🎉 Unlocked! Password: {found}. Press Enter...{C_RESET}")
                else: input(f"\n{C_RED}❌ Password recovery failed. Press Enter...{C_RESET}")

if __name__ == "__main__": main()
