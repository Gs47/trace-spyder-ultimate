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
    print(f"{C_MAGENTA}  [▸] ACTIVE MODULE : {C_GREEN}LIVE CRYPTO & CURRENCY TRACKER{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

import requests

def view_crypto():
    clear_screen()
    print(f"{C_YELLOW}[*] Fetching Real-time Global Crypto Rates...{C_RESET}\n")
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,solana,ripple,tether&vs_currencies=usd,inr"
        res = requests.get(url, timeout=8).json()
        print(f"{C_CYAN}╔══════════════════════ [ LIVE RATES ] ══════════════════════╗{C_RESET}")
        for coin, val in res.items():
            usd, inr = val.get('usd', 0), val.get('inr', 0)
            print(f"  {C_GREEN}▸ {coin.upper():<12}{C_RESET} : {C_WHITE}${usd:<10,}{C_RESET} | {C_YELLOW}₹{inr:<12,}{C_RESET}")
        print(f"{C_CYAN}╚════════════════════════════════════════════════════════════╝{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Crypto API Error: {e}{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Live Crypto Market Ticker (BTC/ETH/SOL/XRP/USDT)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1): {C_RESET}").strip().lower()
        if c == '1': view_crypto()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
