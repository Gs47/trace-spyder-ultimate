import os, sys, shutil, time, socket, json, ssl
import urllib.request
import urllib.error
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

# Bypass local SSL certificate check issues in Termux
SSL_CTX = ssl._create_unverified_context()

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner(sub="NETWORK AUDIT & SCAN"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  NETWORK AUDIT & RECON  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'⚡ ═ G O W R I   S H A N K A R ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{f'🚀 ═ {sub} ═ 🚀'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=6, context=SSL_CTX) as resp:
        return json.loads(resp.read().decode("utf-8"))

def clean_target_input(raw):
    raw = raw.strip()
    if raw.startswith("http://"): raw = raw[7:]
    elif raw.startswith("https://"): raw = raw[8:]
    raw = raw.split("/")[0].split(":")[0].strip()
    return raw

def public_ip_and_geo_audit():
    print_banner("PUBLIC IP & GEOLOCATION AUDIT")
    print(f"{C_WHITE}Press Enter for YOUR Public IP, or enter a target Domain / IP:{C_RESET}")
    print(f"{C_MAGENTA}Examples: ivyparadiseplant.com, 8.8.8.8, google.com{C_RESET}\n")
    
    raw_target = input(f"{C_GREEN}➤ Target [Default: Self IP]: {C_RESET}").strip()
    clean_target = clean_target_input(raw_target)

    resolved_ip = ""
    domain_name = ""

    if clean_target:
        print(f"\n{C_YELLOW}[*] Resolving DNS for target: {clean_target}...{C_RESET}")
        try:
            resolved_ip = socket.gethostbyname(clean_target)
            if resolved_ip != clean_target:
                domain_name = clean_target
            print(f"  {C_GREEN}✔ Resolved IP:{C_RESET} {resolved_ip}")
        except Exception as e:
            print(f"  {C_RED}✖ DNS Resolution Failed: {e}{C_RESET}")
            resolved_ip = clean_target

    print(f"\n{C_YELLOW}[*] Querying global intelligence servers...{C_RESET}")
    data = None
    provider_used = None

    # Provider 1: ipwho.is (Robust for IPs & Domains)
    if not data:
        try:
            url = f"https://ipwho.is/{resolved_ip}" if resolved_ip else "https://ipwho.is/"
            res = fetch_json(url)
            if res.get("success", False):
                data = {
                    "ip": res.get("ip"),
                    "country": f"{res.get('country')} ({res.get('country_code')})",
                    "region": res.get("region"),
                    "city": res.get("city"),
                    "zip": res.get("postal") or "N/A",
                    "lat_lon": f"{res.get('latitude')}, {res.get('longitude')}",
                    "timezone": res.get("timezone", {}).get("id") or "N/A",
                    "isp": res.get("connection", {}).get("isp") or "N/A",
                    "org": res.get("connection", {}).get("org") or res.get("connection", {}).get("asn") or "N/A"
                }
                provider_used = "IPWhois Global Engine"
        except Exception: pass

    # Provider 2: ip-api.com
    if not data:
        try:
            url = f"http://ip-api.com/json/{resolved_ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query" if resolved_ip else "http://ip-api.com/json/?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
            res = fetch_json(url)
            if res.get("status") == "success":
                data = {
                    "ip": res.get("query"),
                    "country": f"{res.get('country')} ({res.get('countryCode')})",
                    "region": res.get("regionName"),
                    "city": res.get("city"),
                    "zip": res.get("zip") or "N/A",
                    "lat_lon": f"{res.get('lat')}, {res.get('lon')}",
                    "timezone": res.get("timezone"),
                    "isp": res.get("isp"),
                    "org": res.get("org") or res.get("as")
                }
                provider_used = "IP-API Core"
        except Exception: pass

    # Provider 3: freeipapi.com
    if not data:
        try:
            url = f"https://freeipapi.com/api/json/{resolved_ip}" if resolved_ip else "https://freeipapi.com/api/json"
            res = fetch_json(url)
            if res.get("ipAddress"):
                data = {
                    "ip": res.get("ipAddress"),
                    "country": f"{res.get('countryName')} ({res.get('countryCode')})",
                    "region": res.get("regionName"),
                    "city": res.get("cityName"),
                    "zip": res.get("zipCode") or "N/A",
                    "lat_lon": f"{res.get('latitude')}, {res.get('longitude')}",
                    "timezone": res.get("timeZone"),
                    "isp": "N/A",
                    "org": "N/A"
                }
                provider_used = "FreeIPApi Engine"
        except Exception: pass

    if not data:
        print(f"\n{C_RED}❌ Error: All Geo-IP intelligence nodes are currently unreachable.{C_RESET}")
        print(f"{C_YELLOW}Tip: Ensure your internet connection is active.{C_RESET}")
        input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")
        return

    print_banner("AUDIT REPORT")
    print(f"{C_WHITE}Intelligence Source:{C_RESET} {C_GREEN}{provider_used}{C_RESET}\n")
    if domain_name:
        print(f"  {C_CYAN}Target Domain  :{C_RESET} {C_YELLOW}{domain_name}{C_RESET}")
    print(f"  {C_CYAN}IP Address     :{C_RESET} {C_WHITE}\033[1m{data.get('ip')}{C_RESET}")
    print(f"  {C_CYAN}Country        :{C_RESET} {C_YELLOW}{data.get('country')}{C_RESET}")
    print(f"  {C_CYAN}Region / State :{C_RESET} {data.get('region')}")
    print(f"  {C_CYAN}City           :{C_RESET} {data.get('city')}")
    print(f"  {C_CYAN}Postal ZIP Code:{C_RESET} {data.get('zip')}")
    print(f"  {C_CYAN}Coordinates    :{C_RESET} {data.get('lat_lon')}")
    print(f"  {C_CYAN}Timezone       :{C_RESET} {data.get('timezone')}")
    print(f"  {C_CYAN}ISP Provider   :{C_RESET} {C_GREEN}{data.get('isp')}{C_RESET}")
    print(f"  {C_CYAN}Organization   :{C_RESET} {data.get('org')}")

    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

def advanced_port_scanner():
    print_banner("PORT SCANNER")
    raw_target = input(f"{C_GREEN}➤ Enter Host or IP (e.g. scanme.org): {C_RESET}").strip()
    target = clean_target_input(raw_target)
    if not target: return

    try:
        target_ip = socket.gethostbyname(target)
    except Exception as e:
        print(f"\n{C_RED}❌ Host resolution failed: {e}{C_RESET}")
        time.sleep(1.5)
        return

    print(f"\n{C_YELLOW}[*] Target IP resolved to: {target_ip}{C_RESET}")
    print(f" {C_CYAN}[1]{C_RESET} Quick Common Ports (21, 22, 80, 443, 8080, 3306)")
    print(f" {C_CYAN}[2]{C_RESET} Standard Top 20 Ports")
    print(f" {C_CYAN}[3]{C_RESET} Custom Port Range (e.g. 1-1000)")
    
    sel = input(f"\n{C_GREEN}➤ Select Scan Profile (1-3): {C_RESET}").strip()
    
    ports = [21, 22, 53, 80, 443, 8080, 3306]
    if sel == '2':
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 8080]
    elif sel == '3':
        r_str = input(f"{C_GREEN}➤ Enter range (e.g. 20-100): {C_RESET}").strip()
        try:
            start_p, end_p = map(int, r_str.split("-"))
            ports = list(range(start_p, end_p + 1))
        except:
            print(f"{C_RED}❌ Invalid range format.{C_RESET}")
            time.sleep(1.2)
            return

    print(f"\n{C_YELLOW}[*] Scanning {len(ports)} port(s) on {target_ip}...{C_RESET}\n")
    open_ports = []
    
    socket.setdefaulttimeout(0.5)
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((target_ip, p))
        if res == 0:
            open_ports.append(p)
            print(f"  {C_GREEN}✔ PORT {p:<5} [OPEN]{C_RESET}")
        s.close()

    print(f"\n{C_WHITE}Scan Complete! Discovered {len(open_ports)} open port(s).{C_RESET}")
    input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def main():
    while True:
        print_banner("NETWORK AUDIT & SCAN")
        print(f" {C_CYAN}[1]{C_RESET} 🌐 \033[1mPublic IP & Geolocation Audit\033[0m")
        print(f" {C_CYAN}[2]{C_RESET} 🔍 \033[1mAdvanced Multi-Port Scanner\033[0m")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Option (1-2 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': public_ip_and_geo_audit()
        elif opt == '2': advanced_port_scanner()

if __name__ == "__main__":
    main()
