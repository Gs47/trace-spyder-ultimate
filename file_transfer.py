#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRACE SPYDER ULTIMATE - MOBILE FIT FILE TRANSFER
Author: Gowri Shankar
"""

import os, sys, socket, shutil, http.server, socketserver

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

SAVE_DIR = "/sdcard/Download/TraceSpyder_Transfers"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
    print(f"{C_WHITE} ⚡ TRACE SPYDER : FILE TRANSFER ENGINE ⚡   {C_RESET}")
    print(f"{C_MAGENTA}      🕷️  BY GOWRI SHANKAR  🕷️                {C_RESET}")
    print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}\n")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def ensure_save_dir():
    if not os.path.exists(SAVE_DIR):
        try: os.makedirs(SAVE_DIR, exist_ok=True)
        except Exception: pass

def check_croc_installed():
    return shutil.which("croc") is not None

def install_croc():
    print(f"\n{C_YELLOW}[*] Installing croc in Termux...{C_RESET}")
    os.system("pkg update -y && pkg install croc -y")
    if check_croc_installed():
        print(f"{C_GREEN}[✓] croc installed successfully!{C_RESET}")
    else:
        print(f"{C_RED}[!] Installation failed.{C_RESET}")
    input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")

def receive_via_croc():
    print_banner()
    if not check_croc_installed():
        print(f"{C_RED}[!] croc is not installed!{C_RESET}")
        print(f"{C_YELLOW}[*] Choose option [4] first.{C_RESET}")
        input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")
        return

    ensure_save_dir()
    print(f"{C_GREEN}╔══════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_GREEN}║ [ RECEIVE FILES VIA CROC ]                   ║{C_RESET}")
    print(f"{C_GREEN}╚══════════════════════════════════════════════╝{C_RESET}")
    print(f"{C_CYAN}[i] Save Path:{C_RESET} {C_YELLOW}{SAVE_DIR}{C_RESET}\n")

    code = input(f"{C_WHITE}➤ Enter Laptop Code: {C_RESET}").strip()
    if not code: return

    print(f"\n{C_YELLOW}[*] Downloading files...{C_RESET}\n")
    os.chdir(SAVE_DIR)
    os.system(f"croc --yes {code}")
    print(f"\n{C_GREEN}[✓] Completed! Check: {SAVE_DIR}{C_RESET}")
    input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")

def send_via_croc():
    print_banner()
    if not check_croc_installed():
        print(f"{C_RED}[!] croc is not installed!{C_RESET}")
        input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")
        return

    print(f"{C_GREEN}╔══════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_GREEN}║ [ SEND FILES VIA CROC ]                      ║{C_RESET}")
    print(f"{C_GREEN}╚══════════════════════════════════════════════╝{C_RESET}\n")

    path = input(f"{C_WHITE}➤ Enter file/folder path: {C_RESET}").strip()
    if not path or not os.path.exists(path):
        print(f"{C_RED}[!] Path not found!{C_RESET}")
        input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")
        return

    os.system(f'croc send "{path}"')
    input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")

class HTTPUploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width, initial-scale=1'><title>Trace Spyder Hub</title><style>body{font-family:sans-serif;background:#0f172a;color:#f8fafc;text-align:center;padding:25px 10px;}.card{background:#1e293b;max-width:500px;margin:0 auto;padding:20px;border-radius:12px;border:1px solid #38bdf8;}h2{color:#38bdf8;font-size:20px;}.box{border:2px dashed #38bdf8;padding:20px;margin:15px 0;background:#0f172a;border-radius:8px;}input{margin:10px 0;color:#cbd5e1;}button{background:#0284c7;color:#fff;border:none;padding:12px 24px;font-size:15px;border-radius:6px;cursor:pointer;font-weight:bold;}</style></head><body><div class='card'><h2>🕷️ TRACE SPYDER HUB 🕷️</h2><p>Select photos from Laptop to upload</p><form action='/upload' method='post' enctype='multipart/form-data'><div class='box'><input type='file' name='files' multiple required></div><button type='submit'>Upload Files</button></form></div></body></html>"""
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/upload':
            ensure_save_dir()
            ctype = self.headers.get('Content-Type', '')
            boundary = None
            for item in ctype.split(';'):
                item = item.strip()
                if item.startswith('boundary='):
                    boundary = item.split('=', 1)[1].strip('"\'').encode('utf-8')
                    break
            count = 0
            if boundary:
                length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(length)
                parts = body.split(b'--' + boundary)
                for part in parts:
                    if not part or part.startswith(b'--'): continue
                    if b'\r\n\r\n' in part:
                        h, c = part.split(b'\r\n\r\n', 1)
                        if c.endswith(b'\r\n'): c = c[:-2]
                        h_str = h.decode('utf-8', errors='ignore')
                        fname = None
                        for line in h_str.splitlines():
                            if 'Content-Disposition:' in line and 'filename=' in line:
                                for sub in line.split(';'):
                                    sub = sub.strip()
                                    if sub.startswith('filename='):
                                        fname = sub.split('=', 1)[1].strip('"\'')
                                        break
                        if fname:
                            fname = os.path.basename(fname)
                            if fname:
                                out = os.path.join(SAVE_DIR, fname)
                                with open(out, 'wb') as f:
                                    f.write(c)
                                count += 1
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            resp = f"""<!DOCTYPE html><html><body style="background:#0f172a;color:#22c55e;text-align:center;padding:40px;font-family:sans-serif;"><h2>✓ Uploaded {count} Files!</h2><p style="color:#fff">Saved: <code>{SAVE_DIR}</code></p><a href="/" style="color:#38bdf8;text-decoration:none;font-weight:bold;">← Upload More</a></body></html>"""
            self.wfile.write(resp.encode('utf-8'))

def start_wifi_upload_hub():
    print_banner()
    ip = get_local_ip()
    port = 8080
    ensure_save_dir()
    print(f"{C_GREEN}╔══════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_GREEN}║ [ WI-FI UPLOAD HUB (LAPTOP ➔ PHONE) ]        ║{C_RESET}")
    print(f"{C_GREEN}╚══════════════════════════════════════════════╝{C_RESET}\n")
    print(f"{C_YELLOW}[!] Connect both to the SAME Wi-Fi / Hotspot!{C_RESET}\n")
    print(f"{C_WHITE}1. Laptop Browser URL:{C_RESET} {C_CYAN}http://{ip}:{port}{C_RESET}")
    print(f"{C_WHITE}2. Select files & click Upload.{C_RESET}\n")
    print(f"{C_MAGENTA}[*] Running... Press Ctrl + C to Stop.{C_RESET}\n")
    try:
        with socketserver.TCPServer(("", port), HTTPUploadHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{C_YELLOW}[!] Server stopped.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}[!] Error: {e}{C_RESET}")
    input(f"\n{C_WHITE}Press Enter to continue...{C_RESET}")

def main():
    while True:
        print_banner()
        print(f"  {C_CYAN}[1]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}Receive via Croc (Laptop Code){C_RESET}")
        print(f"  {C_CYAN}[2]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}Send via Croc{C_RESET}")
        print(f"  {C_CYAN}[3]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}Start Wi-Fi Upload Hub (Browser){C_RESET}")
        print(f"  {C_CYAN}[4]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}Install / Update Croc{C_RESET}")
        print(f"\n{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}[0] 🔙 Back to Master Menu                  {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}")
        try:
            ch = input(f"\n{C_GREEN}➤ Select Option (0-4): {C_RESET}").strip()
            if ch == "1": receive_via_croc()
            elif ch == "2": send_via_croc()
            elif ch == "3": start_wifi_upload_hub()
            elif ch == "4": install_croc()
            elif ch in ["0", "x", "q", "b"]: break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
