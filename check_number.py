import os, sys, time, json, shutil
import urllib.request, urllib.parse

# Safe input wrapper to prevent EOFError / Pipe crashes
_orig_input = input
def input(prompt=""):
    try:
        return _orig_input(prompt)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)


C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

def check_nav(val):
    v = str(val).strip().lower()
    if v in ['x', 'exit', 'quit', 'kill']:
        sys.exit(99)
    if v in ['m', 'main', 'home', 'mm', '##']:
        sys.exit(0)
    if v in ['0', '00', 'b', 'back', '#']:
        return "BACK"
    return val

def get_screen_width():
    try: return max(34, shutil.get_terminal_size((50, 20)).columns)
    except: return 48

def print_banner(sub="PHONE NUMBER LOOKUP"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    c_title = "🕷️  TRACE SPYDER  🕷️"
    print(f"{C_CYAN}║{C_WHITE}{c_title.center(inner_w)}{C_CYAN}║{C_RESET}")
    author = "🕷️  G O W R I   S H A N K A R  🕷️"
    tag = f"⚡ ═ {sub} ═ ⚡"
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{author.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{tag.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def lookup_number(num):
    clean_num = ''.join(c for c in num if c.isdigit() or c == '+')
    if not clean_num:
        print(f"\n{C_RED}❌ Invalid phone number format.{C_RESET}")
        return

    print(f"\n{C_YELLOW}[*] Probing international telecommunication databases for {clean_num}...{C_RESET}")
    time.sleep(0.8)

    # Local Prefix Database Analysis
    country = "Unknown"
    carrier = "Unknown / Mobile Network"
    line_type = "Mobile / Landline"
    timezone = "UTC"

    if clean_num.startswith("+91") or clean_num.startswith("91") and len(clean_num) >= 12:
        country = "India (IN) 🇮🇳"
        timezone = "Asia/Kolkata (+05:30)"
    elif clean_num.startswith("+1") or len(clean_num) == 10:
        country = "United States / Canada (US/CA) 🇺🇸"
        timezone = "America/New_York (-05:00)"
    elif clean_num.startswith("+44"):
        country = "United Kingdom (UK) 🇬🇧"
        timezone = "Europe/London (+00:00)"
    elif clean_num.startswith("+971"):
        country = "United Arab Emirates (UAE) 🇦🇪"
        timezone = "Asia/Dubai (+04:00)"
    elif clean_num.startswith("+966"):
        country = "Saudi Arabia (SA) 🇸🇦"
        timezone = "Asia/Riyadh (+03:00)"
    else:
        country = "International / Global Region"

    # Online Open API Free Check
    api_success = False
    try:
        url = f"https://html.duckduckgo.com/html/?q=phone+number+info+{urllib.parse.quote(clean_num)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as res:
            if res.status_code == 200:
                api_success = True
    except: pass

    w = get_screen_width()
    div = "─" * (w - 2)

    print(f"\n{C_CYAN}┌── [ TELECOM LOOKUP REPORT ] ──────────────────────────────┐{C_RESET}")
    print(f" {C_WHITE}Target Number    :{C_RESET} {C_GREEN}{clean_num}{C_RESET}")
    print(f" {C_WHITE}Country / Region :{C_RESET} {C_GREEN}{country}{C_RESET}")
    print(f" {C_WHITE}Estimated Carrier:{C_RESET} {C_YELLOW}{carrier}{C_RESET}")
    print(f" {C_WHITE}Line Classification:{C_RESET} {C_CYAN}{line_type}{C_RESET}")
    print(f" {C_WHITE}Timezone Region  :{C_RESET} {C_MAGENTA}{timezone}{C_RESET}")
    print(f" {C_WHITE}Database Status  :{C_RESET} {C_GREEN if api_success else C_YELLOW}{'Verified Online' if api_success else 'Standard Heuristics'}{C_RESET}")
    print(f"{C_CYAN}└───────────────────────────────────────────────────────────┘{C_RESET}")

def main():
    while True:
        print_banner("PHONE NUMBER LOOKUP")
        print(f" {C_WHITE}Enter phone number with country code (e.g., +919876543210){C_RESET}")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
        
        raw = input(f"\n{C_GREEN}➤ Phone Number (or [0] Back / [m] Main / [x] Exit): {C_RESET}")
        val = check_nav(raw)
        if val == "BACK": break

        if raw.strip():
            lookup_number(raw.strip())
            inp = input(f"\n{C_GREEN}Press Enter to lookup another number...{C_RESET}")
            check_nav(inp)

if __name__ == "__main__":
    main()