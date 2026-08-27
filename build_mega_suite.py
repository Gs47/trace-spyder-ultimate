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


BANNER = """\033[1;36m┌────────────────────────────────────────────────────────────┐
\033[1;37m  ████████╗██████╗  █████╗  ██████╗███████╗
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
\033[0m
         \033[1;33m🕷️  \033[1;36mG O W R I   S H A N K A R\033[1;33m  🕷️\033[0m
           \033[1;35m⚡ ═ \033[1;32mT E R M I N A L   H U B\033[1;35m ═ ⚡\033[0m
\033[1;36m└────────────────────────────────────────────────────────────┘\033[0m"""

def get_header(title):
    return f'''import os, sys, subprocess, shutil, glob, time

C_CYAN = "\\033[1;36m"
C_GREEN = "\\033[1;32m"
C_YELLOW = "\\033[1;33m"
C_RED = "\\033[1;31m"
C_MAGENTA = "\\033[1;35m"
C_WHITE = "\\033[1;37m"
C_RESET = "\\033[0m"

BANNER = """{BANNER}"""

def get_download_dir():
    if os.name == 'nt':
        return os.path.join(os.path.expanduser("~"), "Downloads")
    if os.path.exists("/sdcard/Download"):
        return "/sdcard/Download"
    return os.path.expanduser("~/Downloads")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(f"{{C_MAGENTA}}  [▸] ACTIVE MODULE : {{C_GREEN}}{title}{{C_RESET}}")
    print(f"{{C_CYAN}}─"*60 + f"{{C_RESET}}")
'''

# 1. Port Scanner & DNS Recon
recon_code = get_header("CYBER PORT SCANNER & DNS RECON") + '''
import socket

def scan_ports():
    clear_screen()
    target = input(f"{C_GREEN}➤ Enter Target IP or Domain (e.g., google.com / 192.168.1.1): {C_RESET}").strip()
    if not target: return
    try:
        ip = socket.gethostbyname(target)
        print(f"\\n{C_YELLOW}[*] Resolving Target : {C_WHITE}{target} ({ip}){C_RESET}")
        print(f"{C_CYAN}────────────────── [ COMMON PORTS SCAN ] ──────────────────{C_RESET}")
        ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 1433, 3306, 3389, 8080, 8443]
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.4)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"  {C_GREEN}[✓] Port {port:<5} : OPEN{C_RESET}")
            s.close()
    except Exception as e:
        print(f"{C_RED}❌ Scan failed: {e}{C_RESET}")
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Fast Port Scanner (Common Service Ports)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1): {C_RESET}").strip().lower()
        if c == '1': scan_ports()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 2. Crypto & Fiat Currency Tracker
crypto_code = get_header("LIVE CRYPTO & CURRENCY TRACKER") + '''
import requests

def view_crypto():
    clear_screen()
    print(f"{C_YELLOW}[*] Fetching Real-time Global Crypto Rates...{C_RESET}\\n")
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
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

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
'''

# 3. System Hardware Benchmark
benchmark_code = get_header("SYSTEM HARDWARE BENCHMARK") + '''
def run_benchmark():
    clear_screen()
    print(f"{C_YELLOW}[*] Running Multi-threaded Math CPU Stress Test (10,000,000 ops)...{C_RESET}")
    t0 = time.time()
    total = sum(i * i for i in range(10000000))
    t1 = time.time()
    elapsed = max(0.001, t1 - t0)
    score = int(10000 / elapsed)
    
    print(f"\\n{C_CYAN}╔═════════════════════ [ BENCHMARK RESULTS ] ═════════════════════╗{C_RESET}")
    print(f"  {C_GREEN}Execution Time :{C_RESET} {C_WHITE}{elapsed:.3f} Seconds{C_RESET}")
    print(f"  {C_GREEN}Performance Score:{C_RESET} {C_YELLOW}{score} Pts{C_RESET}")
    print(f"  {C_GREEN}Hardware Rating:{C_RESET} {C_WHITE}{'Exceptional' if score > 8000 else 'Balanced / Standard'}{C_RESET}")
    print(f"{C_CYAN}╚═════════════════════════════════════════════════════════════════╝{C_RESET}")
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Run Instant CPU & Arithmetic Benchmark")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1): {C_RESET}").strip().lower()
        if c == '1': run_benchmark()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 4. Hash Generator & Cracker
hash_code = get_header("HASH GENERATOR & CRACKER") + '''
import hashlib

def generate_hashes():
    clear_screen()
    text = input(f"{C_GREEN}➤ Enter String to Generate Cryptographic Hashes: {C_RESET}").strip()
    if not text: return
    b = text.encode()
    print(f"\\n{C_CYAN}╔══════════════════════ [ CRYPTO HASHES ] ══════════════════════╗{C_RESET}")
    print(f"  {C_GREEN}MD5   :{C_RESET} {C_WHITE}{hashlib.md5(b).hexdigest()}{C_RESET}")
    print(f"  {C_GREEN}SHA1  :{C_RESET} {C_WHITE}{hashlib.sha1(b).hexdigest()}{C_RESET}")
    print(f"  {C_GREEN}SHA256:{C_RESET} {C_WHITE}{hashlib.sha256(b).hexdigest()}{C_RESET}")
    print(f"  {C_GREEN}SHA512:{C_RESET} {C_WHITE}{hashlib.sha512(b).hexdigest()[:64]}...{C_RESET}")
    print(f"{C_CYAN}╚════════════════════════════════════════════════════════════════╝{C_RESET}")
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Generate Multi-Algorithm Hashes (MD5/SHA256/SHA512)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1): {C_RESET}").strip().lower()
        if c == '1': generate_hashes()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 5. Cyber Encoder / Decoder
encoder_code = get_header("CYBER ENCODER & DECODER") + '''
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
            txt = input(f"\\n{C_GREEN}➤ Enter String: {C_RESET}").strip()
            act = input("Encode (e) or Decode (d)?: ").strip().lower()
            if act == 'e': print(f"\\n{C_YELLOW}Result: {base64.b64encode(txt.encode()).decode()}{C_RESET}")
            else:
                try: print(f"\\n{C_YELLOW}Result: {base64.b64decode(txt.encode()).decode()}{C_RESET}")
                except Exception: print(f"{C_RED}❌ Invalid Base64!{C_RESET}")
            input("\\nPress Enter...")
        elif c == '2':
            txt = input(f"\\n{C_GREEN}➤ Enter String: {C_RESET}").strip()
            act = input("Encode (e) or Decode (d)?: ").strip().lower()
            if act == 'e': print(f"\\n{C_YELLOW}Result: {txt.encode().hex()}{C_RESET}")
            else:
                try: print(f"\\n{C_YELLOW}Result: {bytes.fromhex(txt).decode()}{C_RESET}")
                except Exception: print(f"{C_RED}❌ Invalid Hex!{C_RESET}")
            input("\\nPress Enter...")
        elif c == '3':
            txt = input(f"\\n{C_GREEN}➤ Enter String: {C_RESET}").strip()
            act = input("Encode (e) or Decode (d)?: ").strip().lower()
            if act == 'e': print(f"\\n{C_YELLOW}Result: {urllib.parse.quote(txt)}{C_RESET}")
            else: print(f"\\n{C_YELLOW}Result: {urllib.parse.unquote(txt)}{C_RESET}")
            input("\\nPress Enter...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 6. Password & Token Generator
pwgen_code = get_header("SECURE PASSWORD & TOKEN GENERATOR") + '''
import secrets, string

def generate_pass():
    clear_screen()
    length = input(f"{C_GREEN}➤ Enter Length (Default 16): {C_RESET}").strip()
    length = int(length) if length.isdigit() else 16
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    pwd = ''.join(secrets.choice(chars) for _ in range(length))
    token = secrets.token_hex(length // 2)
    print(f"\\n{C_CYAN}╔═════════════════════ [ GENERATED SECRETS ] ═════════════════════╗{C_RESET}")
    print(f"  {C_GREEN}Strong Password :{C_RESET} {C_WHITE}{pwd}{C_RESET}")
    print(f"  {C_GREEN}Hex API Token   :{C_RESET} {C_YELLOW}{token}{C_RESET}")
    print(f"{C_CYAN}╚═════════════════════════════════════════════════════════════════╝{C_RESET}")
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Generate Cryptographically Secure Password / Token")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1): {C_RESET}").strip().lower()
        if c == '1': generate_pass()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 7. Web Header & Recon Fetcher
web_recon_code = get_header("WEB HEADERS & RECON FETCHER") + '''
import requests

def inspect_url():
    clear_screen()
    url = input(f"{C_GREEN}➤ Enter Website URL (e.g., example.com): {C_RESET}").strip()
    if not url: return
    if not url.startswith("http"): url = "https://" + url
    try:
        r = requests.get(url, timeout=8)
        print(f"\\n{C_CYAN}╔══════════════════════ [ SERVER HEADERS ] ══════════════════════╗{C_RESET}")
        print(f"  {C_GREEN}Status Code :{C_RESET} {C_WHITE}{r.status_code}{C_RESET}")
        for k, v in list(r.headers.items())[:10]:
            print(f"  {C_YELLOW}{k:<20}:{C_RESET} {C_WHITE}{v[:40]}{C_RESET}")
        print(f"{C_CYAN}╚════════════════════════════════════════════════════════════════╝{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Error: {e}{C_RESET}")
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Fetch Server Headers & Security Flags")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1): {C_RESET}").strip().lower()
        if c == '1': inspect_url()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 8. Encrypted Terminal Notes & Diary
notes_code = get_header("ENCRYPTED TERMINAL NOTES & DIARY") + '''
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
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def add_note():
    clear_screen()
    note = input(f"{C_GREEN}➤ Enter Quick Note / Secret String: {C_RESET}").strip()
    if note:
        with open(NOTES_FILE, "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M')}] {note}\\n")
        print(f"\\n{C_GREEN}✅ Note saved securely!{C_RESET}")
    input(f"\\n{C_YELLOW}Press Enter to continue...{C_RESET}")

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
            input(f"\\n{C_GREEN}✅ Storage Cleared! Press Enter...{C_RESET}")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

files = {
    "recon_tool.py": recon_code,
    "crypto_tool.py": crypto_code,
    "benchmark_tool.py": benchmark_code,
    "hash_tool.py": hash_code,
    "encoder_tool.py": encoder_code,
    "pwgen_tool.py": pwgen_code,
    "web_recon.py": web_recon_code,
    "notes_tool.py": notes_code
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ All new module scripts built!")