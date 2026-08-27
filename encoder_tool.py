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
    print(f"{C_MAGENTA}  [▸] ACTIVE MODULE : {C_GREEN}CYBER ENCODER & DECODER{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

import base64, urllib.parse

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Base64 Encode / Decode")
        print(f"  {C_CYAN}[2]{C_RESET} Hex (Hexadecimal) Encode / Decode")
        print(f"  {C_CYAN}[3]{C_RESET} URL Percent Encode / Decode")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1-3): {C_RESET}").strip().lower()
        if c == '1':
            txt = input(f"\n{C_GREEN}➤ Enter String: {C_RESET}").strip()
            act = input("Encode (e) or Decode (d)?: ").strip().lower()
            if act == 'e': print(f"\n{C_YELLOW}Result: {base64.b64encode(txt.encode()).decode()}{C_RESET}")
            else:
                try: print(f"\n{C_YELLOW}Result: {base64.b64decode(txt.encode()).decode()}{C_RESET}")
                except Exception: print(f"{C_RED}❌ Invalid Base64!{C_RESET}")
            input("\nPress Enter...")
        elif c == '2':
            txt = input(f"\n{C_GREEN}➤ Enter String: {C_RESET}").strip()
            act = input("Encode (e) or Decode (d)?: ").strip().lower()
            if act == 'e': print(f"\n{C_YELLOW}Result: {txt.encode().hex()}{C_RESET}")
            else:
                try: print(f"\n{C_YELLOW}Result: {bytes.fromhex(txt).decode()}{C_RESET}")
                except Exception: print(f"{C_RED}❌ Invalid Hex!{C_RESET}")
            input("\nPress Enter...")
        elif c == '3':
            txt = input(f"\n{C_GREEN}➤ Enter String: {C_RESET}").strip()
            act = input("Encode (e) or Decode (d)?: ").strip().lower()
            if act == 'e': print(f"\n{C_YELLOW}Result: {urllib.parse.quote(txt)}{C_RESET}")
            else: print(f"\n{C_YELLOW}Result: {urllib.parse.unquote(txt)}{C_RESET}")
            input("\nPress Enter...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
