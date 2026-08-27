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

# 1. New: Network Speedtest & IP Info
net_tools_code = get_header("NETWORK SPEEDTEST & IP EXPLORER") + '''
import requests

def run_speedtest():
    clear_screen()
    print(f"{C_YELLOW}[*] Testing Network Latency, Download & Upload Speed...{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")
    try:
        import speedtest
        st = speedtest.Speedtest()
        print(f"[*] Selecting optimal server...")
        st.get_best_server()
        ping = st.results.ping
        print(f"  {C_GREEN}[✓]{C_RESET} Ping Latency : {C_WHITE}{ping:.2f} ms{C_RESET}")
        
        print(f"[*] Testing Download Speed...")
        dl = st.download() / (1024 * 1024)
        print(f"  {C_GREEN}[✓]{C_RESET} Download Speed: {C_YELLOW}{dl:.2f} Mbps{C_RESET}")
        
        print(f"[*] Testing Upload Speed...")
        ul = st.upload() / (1024 * 1024)
        print(f"  {C_GREEN}[✓]{C_RESET} Upload Speed  : {C_MAGENTA}{ul:.2f} Mbps{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Speedtest error: {e}{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")
    input("Press Enter to continue...")

def get_ip_info():
    clear_screen()
    print(f"{C_YELLOW}[*] Fetching Public IP & Geolocation Details...{C_RESET}\n")
    try:
        r = requests.get("https://ipapi.co/json/", timeout=8).json()
        print(f"  {C_CYAN}Public IP Address :{C_RESET} {C_WHITE}{r.get('ip')}{C_RESET}")
        print(f"  {C_CYAN}ISP / Organization:{C_RESET} {C_WHITE}{r.get('org')}{C_RESET}")
        print(f"  {C_CYAN}City / Region     :{C_RESET} {C_WHITE}{r.get('city')}, {r.get('region')}{C_RESET}")
        print(f"  {C_CYAN}Country           :{C_RESET} {C_WHITE}{r.get('country_name')} ({r.get('country_code')}){C_RESET}")
        print(f"  {C_CYAN}Timezone          :{C_RESET} {C_WHITE}{r.get('timezone')}{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Error fetching IP: {e}{C_RESET}")
    print(f"\n{C_CYAN}─"*60 + f"{C_RESET}")
    input("Press Enter to continue...")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Live Speedtest (Ping / Download / Upload)")
        print(f"  {C_CYAN}[2]{C_RESET} Public IP & Network Geolocation Details")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1-2): {C_RESET}").strip().lower()
        if c == '1': run_speedtest()
        elif c == '2': get_ip_info()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 2. New: QR Code Generator & Terminal Renderer
qr_code_tool = get_header("TERMINAL QR CODE ENGINE") + '''
import qrcode

def generate_qr():
    clear_screen()
    data = input(f"{C_GREEN}➤ Enter Text or URL to generate QR: {C_RESET}").strip()
    if not data: return
    
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()
    
    print(f"\n{C_YELLOW}[*] Displaying Terminal QR Code:{C_RESET}\n")
    qr.print_ascii(invert=True)
    
    save_opt = input(f"\n{C_GREEN}➤ Save as PNG Image in Downloads? (y/n): {C_RESET}").strip().lower()
    if save_opt == 'y':
        out_path = os.path.join(get_download_dir(), "qr_generated.png")
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(out_path)
        print(f"{C_GREEN}✅ Saved: {out_path}{C_RESET}")
    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Generate & View Terminal ASCII QR Code")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1): {C_RESET}").strip().lower()
        if c == '1': generate_qr()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 3. New: File Encryption & Decryption Vault (AES-256)
vault_code = get_header("AES-256 FILE SECURITY VAULT") + '''
import base64, hashlib
from cryptography.fernet import Fernet

def get_key_from_password(password: str) -> bytes:
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file():
    clear_screen()
    fp = input(f"{C_GREEN}➤ Enter File Path to Encrypt: {C_RESET}").strip().strip("\'\\"")
    if not os.path.exists(fp):
        input(f"{C_RED}❌ File not found! Press Enter...{C_RESET}")
        return
    pwd = input(f"{C_GREEN}➤ Enter Secure Password: {C_RESET}").strip()
    if not pwd: return

    f = Fernet(get_key_from_password(pwd))
    with open(fp, 'rb') as file:
        data = file.read()
    encrypted = f.encrypt(data)
    out_file = fp + ".locked"
    with open(out_file, 'wb') as file:
        file.write(encrypted)
    
    os.remove(fp)
    print(f"\n{C_GREEN}🔒 File Encrypted & Original Deleted: {out_file}{C_RESET}")
    input("Press Enter to continue...")

def decrypt_file():
    clear_screen()
    fp = input(f"{C_GREEN}➤ Enter .locked File Path to Decrypt: {C_RESET}").strip().strip("\'\\"")
    if not os.path.exists(fp):
        input(f"{C_RED}❌ File not found! Press Enter...{C_RESET}")
        return
    pwd = input(f"{C_GREEN}➤ Enter Password: {C_RESET}").strip()
    if not pwd: return

    try:
        f = Fernet(get_key_from_password(pwd))
        with open(fp, 'rb') as file:
            data = file.read()
        decrypted = f.decrypt(data)
        out_file = fp.replace(".locked", "")
        with open(out_file, 'wb') as file:
            file.write(decrypted)
        os.remove(fp)
        print(f"\n{C_GREEN}🔓 File Decrypted Successfully: {out_file}{C_RESET}")
    except Exception:
        print(f"\n{C_RED}❌ Decryption failed! Wrong password or corrupted file.{C_RESET}")
    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Lock & Encrypt File (AES-256)")
        print(f"  {C_CYAN}[2]{C_RESET} Unlock & Decrypt File (.locked)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1-2): {C_RESET}").strip().lower()
        if c == '1': encrypt_file()
        elif c == '2': decrypt_file()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 4. New: Link Expander / Unshortener
unshortener_code = get_header("LINK EXPANDER & SAFETY CHECKER") + '''
import requests

def unshorten():
    clear_screen()
    url = input(f"{C_GREEN}➤ Enter Short URL (bit.ly, tinyurl, etc): {C_RESET}").strip()
    if not url: return
    if not url.startswith("http"): url = "https://" + url

    print(f"\n{C_YELLOW}[*] Tracing URL redirects safely...{C_RESET}")
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        print(f"\n{C_CYAN}╔════════════════════════════════════════════════════════════╗{C_RESET}")
        print(f"  {C_GREEN}🔗 Original Destination URL:{C_RESET}")
        print(f"  {C_WHITE}{r.url}{C_RESET}")
        print(f"  {C_CYAN}Status Code:{C_RESET} {r.status_code}")
        print(f"{C_CYAN}╚════════════════════════════════════════════════════════════╝{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Trace failed: {e}{C_RESET}")
    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Unshorten & Inspect Link")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1): {C_RESET}").strip().lower()
        if c == '1': unshorten()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

# 5. Master Dashboard (menu.py) - Complete & Alphabetical
master_menu_code = get_header("MAIN DASHBOARD (ALL-IN-ONE SUITE)") + '''
def run_script(script_name):
    path = os.path.expanduser(f"~/{script_name}")
    if os.path.exists(path):
        subprocess.run([sys.executable, path])
    else:
        print(f"\\n{C_RED}❌ Error: {script_name} not found!{C_RESET}")
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        print(f"  {C_YELLOW}─── [ ALL-IN-ONE CORE UTILITIES (A-Z) ] ───{C_RESET}")
        print(f"  {C_CYAN}[1]{C_RESET}  Archive ZIP Master (Create / Extract / Unlock)")
        print(f"  {C_CYAN}[2]{C_RESET}  Device Battery Diagnostic Status")
        print(f"  {C_CYAN}[3]{C_RESET}  File Security Vault (AES-256 Encrypt / Decrypt)")
        print(f"  {C_CYAN}[4]{C_RESET}  Link Expander & Unshortener (Safety Trace)")
        print(f"  {C_CYAN}[5]{C_RESET}  Media Document Converter Engine (FFmpeg & Images)")
        print(f"  {C_CYAN}[6]{C_RESET}  Network Speedtest & Public IP Info")
        print(f"  {C_CYAN}[7]{C_RESET}  QR Code Terminal Engine (Create & View)")
        print(f"  {C_CYAN}[8]{C_RESET}  Seeker OSINT Location Explorer")
        print(f"  {C_CYAN}[9]{C_RESET}  Spotify Smart Music Video Downloader")
        print(f"  {C_CYAN}[10]{C_RESET} System Auto Repair Diagnostics")
        print(f"  {C_CYAN}[11]{C_RESET} Telegram Cloud Hub (Multi Account Sync)")
        print(f"  {C_CYAN}[12]{C_RESET} Temporary Disposable Email Live Inbox")
        print(f"  {C_CYAN}[13]{C_RESET} TeraBox Fast Video Downloader")
        print(f"  {C_CYAN}[14]{C_RESET} Termux Storage & App Cache Purger")
        print(f"  {C_CYAN}[15]{C_RESET} Universal Media Downloader (YT/IG/FB/X/etc)")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
        print(f"  {C_MAGENTA}⚙️  [16] CONTROL SETTINGS HUB (Updates & Config){C_RESET}")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
        print(f"  {C_YELLOW}[0]{C_RESET}  Refresh Dashboard")
        print(f"  {C_RED}[*]{C_RESET}  Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        choice = input(f"{C_GREEN}➤ Select Module (1-16): {C_RESET}").strip().lower()
        mapping = {
            '1': 'zip_master.py', '01': 'zip_master.py',
            '2': 'device_info.py', '02': 'device_info.py',
            '3': 'file_vault.py', '03': 'file_vault.py',
            '4': 'link_unshort.py', '04': 'link_unshort.py',
            '5': 'converter.py', '05': 'converter.py',
            '6': 'net_tools.py', '06': 'net_tools.py',
            '7': 'qr_tool.py', '07': 'qr_tool.py',
            '8': 'seeker_hub.py', '08': 'seeker_hub.py',
            '9': 'spotify_dl.py', '09': 'spotify_dl.py',
            '10': 'auto_repair.py',
            '11': 'tools.py',
            '12': 'temp_mail.py',
            '13': 'terabox_dl.py',
            '14': 'phone_cleaner.py',
            '15': 'media_dl.py',
            '16': 'settings.py'
        }
        if choice in mapping:
            run_script(mapping[choice])
        elif choice == '0':
            continue
        elif choice in ['*', 'x', 'exit', 'q']:
            print(f"\\n{C_RED}Exiting Trace Spyder Hub. Goodbye!{C_RESET}\\n")
            sys.exit(0)
        else:
            input(f"\\n{C_RED}❌ Invalid selection! Press Enter...{C_RESET}")

if __name__ == "__main__":
    main_menu()
'''

files = {
    "net_tools.py": net_tools_code,
    "qr_tool.py": qr_code_tool,
    "file_vault.py": vault_code,
    "link_unshort.py": unshortener_code,
    "menu.py": master_menu_code
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ Complete All-In-One Power Suite configured successfully!")