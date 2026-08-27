import os, sys, shutil, time, socket, json, ssl
import urllib.request
import urllib.error
from datetime import datetime
import builtins

def safe_input(prompt=""):
    try: return _orig_input(prompt)
    except (EOFError, KeyboardInterrupt): sys.exit(0)
_orig_input = builtins.input
builtins.input = safe_input

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
SSL_CTX = ssl._create_unverified_context()

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner(sub="WEB DOMAIN RECON"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  TRACE SPYDER WEB RECON  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'⚡ ═ G O W R I   S H A N K A R ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{f'🚀 ═ {sub} ═ 🚀'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def clean_domain(url):
    url = url.strip()
    if url.startswith("http://"): url = url[7:]
    elif url.startswith("https://"): url = url[8:]
    return url.split("/")[0].split(":")[0].strip()

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=6, context=SSL_CTX) as resp:
        return json.loads(resp.read().decode("utf-8"))

def full_website_audit():
    print_banner("FULL WEBSITE INTELLIGENCE AUDIT")
    target = input(f"{C_GREEN}➤ Enter Website Domain (e.g. example.com): {C_RESET}").strip()
    domain = clean_domain(target)
    if not domain: return

    print(f"\n{C_YELLOW}[*] Performing Deep Reconnaissance on: {domain}...{C_RESET}\n")

    # 1. DNS & Host Resolution
    ip = ""
    try:
        ip = socket.gethostbyname(domain)
        print(f"  {C_CYAN}[+] IP Address       :{C_RESET} {C_WHITE}\033[1m{ip}{C_RESET}")
    except Exception as e:
        print(f"  {C_RED}[!] DNS Resolution Error: {e}{C_RESET}")

    # 2. HTTP & Server Header Inspection
    target_url = f"https://{domain}"
    try:
        req = urllib.request.Request(target_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6, context=SSL_CTX) as resp:
            status = resp.status
            headers = dict(resp.headers)
            print(f"  {C_CYAN}[+] HTTP Status Code :{C_RESET} {C_GREEN}{status} OK{C_RESET}")
            print(f"  {C_CYAN}[+] Web Server       :{C_RESET} {C_YELLOW}{headers.get('Server', 'Hidden / Cloudflare')}{C_RESET}")
            print(f"  {C_CYAN}[+] Content Type     :{C_RESET} {headers.get('Content-Type', 'N/A')}")
            print(f"  {C_CYAN}[+] Content Encoding :{C_RESET} {headers.get('Content-Encoding', 'None')}")
            print(f"  {C_CYAN}[+] Strict-Transport :{C_RESET} {headers.get('Strict-Transport-Security', 'Not Enforced')}")
    except urllib.error.HTTPError as he:
        print(f"  {C_CYAN}[+] HTTP Status      :{C_RESET} {C_YELLOW}{he.code} {he.reason}{C_RESET}")
    except Exception:
        print(f"  {C_YELLOW}[!] HTTPS check failed, website might be using HTTP only.{C_RESET}")

    # 3. SSL/TLS Certificate Audit
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                issuer = dict(x[0] for x in cert.get('issuer', []))
                common_name = issuer.get('commonName') or issuer.get('organizationName', 'Unknown')
                not_after = cert.get('notAfter', 'Unknown')
                print(f"  {C_CYAN}[+] SSL Issuer       :{C_RESET} {C_GREEN}{common_name}{C_RESET}")
                print(f"  {C_CYAN}[+] SSL Expiry Date  :{C_RESET} {C_YELLOW}{not_after}{C_RESET}")
    except Exception:
        print(f"  {C_YELLOW}[+] SSL Certificate  : Not Detected / Port 443 Closed{C_RESET}")

    # 4. Geolocation & Hosting Intelligence
    if ip:
        try:
            geo = fetch_json(f"https://ipwho.is/{ip}")
            if geo.get("success", False):
                print(f"  {C_CYAN}[+] Hosting Country  :{C_RESET} {geo.get('country')} ({geo.get('country_code')})")
                print(f"  {C_CYAN}[+] Hosting Region   :{C_RESET} {geo.get('region')}, {geo.get('city')}")
                print(f"  {C_CYAN}[+] ISP / ASN        :{C_RESET} {C_GREEN}{geo.get('connection', {}).get('isp')}{C_RESET}")
                print(f"  {C_CYAN}[+] Organization     :{C_RESET} {geo.get('connection', {}).get('org')}")
        except Exception: pass

    # 5. Robots.txt & Sitemap Status
    try:
        rob_req = urllib.request.Request(f"https://{domain}/robots.txt", headers=HEADERS)
        with urllib.request.urlopen(rob_req, timeout=4, context=SSL_CTX) as r_resp:
            if r_resp.status == 200:
                print(f"  {C_CYAN}[+] Robots.txt       :{C_RESET} {C_GREEN}Available (/robots.txt){C_RESET}")
    except Exception:
        print(f"  {C_CYAN}[+] Robots.txt       :{C_RESET} {C_YELLOW}Not Found / Restricted{C_RESET}")

    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

def main():
    while True:
        print_banner("WEB DOMAIN RECON")
        print(f" {C_CYAN}[1]{C_RESET} 🌐 \033[1mFull Website Intelligence Audit\033[0m")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Option (1 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': full_website_audit()

if __name__ == "__main__":
    main()
