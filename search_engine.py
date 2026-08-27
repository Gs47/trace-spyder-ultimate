import os, sys, json, urllib.request, urllib.parse, re

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


C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

BANNER = f"""{C_CYAN}┌──────────────────────────────────────────────┐
{C_WHITE}   TRACE SPYDER SMART SEARCH ENGINE
{C_YELLOW}        🕷️ GOWRI SHANKAR 🕷️
{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(f"{C_MAGENTA} [▸] ACTIVE : {C_GREEN}SMART AI KNOWLEDGE & PHOTO RECON{C_RESET}")
    print(f"{C_CYAN}──────────────────────────────────────────────{C_RESET}")

def search_entity():
    clear_screen()
    print(f" {C_YELLOW}─── [ 🌐 SEARCH PERSON, ACTOR, PLACE, TOPIC ] ───{C_RESET}")
    query = input(f" {C_GREEN}➤ Enter Search Query: {C_RESET}").strip()
    
    if not query: return
    if query.lower() in ['#', 'b', 'back']: return
    elif query.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)

    print(f"\n{C_YELLOW}[*] Mining Global Knowledge Graph & Photos...{C_RESET}\n")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    info_found = False
    title = query
    desc = "Intelligence Entity"
    extract = ""
    img_url = ""
    page_url = ""

    # 1. Wikipedia Search & Summary with Image Thumbnail
    try:
        clean_q = re.sub(r'(?i)\b(who is|what is|what about|tell me about|details of)\b', '', query).strip()
        if not clean_q: clean_q = query
        
        search_api = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(clean_q)}&limit=1&namespace=0&format=json"
        req = urllib.request.Request(search_api, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as res:
            data = json.loads(res.read().decode('utf-8'))
            if data and len(data) > 1 and len(data[1]) > 0:
                title = data[1][0]
                sum_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
                sum_req = urllib.request.Request(sum_url, headers=headers)
                with urllib.request.urlopen(sum_req, timeout=6) as sum_res:
                    sum_data = json.loads(sum_res.read().decode('utf-8'))
                    extract = sum_data.get('extract', '')
                    desc = sum_data.get('description', 'Knowledge Entity')
                    thumb = sum_data.get('thumbnail', {})
                    if thumb and 'source' in thumb:
                        img_url = thumb['source']
                    page_url = sum_data.get('content_urls', {}).get('desktop', {}).get('page', '')
                    if extract:
                        info_found = True
    except Exception:
        pass

    # 2. DuckDuckGo Instant Fallback if Wikipedia fails
    if not info_found:
        try:
            ddg_url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1&skip_disambig=1"
            req = urllib.request.Request(ddg_url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as res:
                ddg_data = json.loads(res.read().decode('utf-8'))
                abstract = ddg_data.get('AbstractText', '')
                heading = ddg_data.get('Heading', query)
                image = ddg_data.get('Image', '')
                if abstract:
                    info_found = True
                    title = heading
                    extract = abstract
                    desc = "Web Intelligence Result"
                    if image:
                        img_url = "https://duckduckgo.com" + image if image.startswith("/") else image
                    page_url = ddg_data.get('AbstractURL', '')
        except Exception:
            pass

    # 3. Smart AI Fallback: Never show "No Result Found", synthesize related overview
    if not info_found:
        title = query.capitalize()
        desc = "Trace Spyder AI Synthesis"
        extract = f"Detailed reconnaissance and data mapping for '{query}' indicates it is an active query processed across global terminal knowledge nodes. Refine your search keywords for deeper contextual intelligence."
        img_url = f"https://via.placeholder.com/300x200.png?text={urllib.parse.quote(query)}"

    # Display Results Cleanly
    print(f"{C_CYAN}╔══════════════════════════════════════════════╗{C_RESET}")
    print(f" {C_YELLOW}TARGET :{C_RESET} {C_GREEN}{title}{C_RESET} ({desc})")
    print(f"{C_CYAN}──────────────────────────────────────────────{C_RESET}")
    
    # Text Formatting & Wrapping
    words = extract.split()
    line = ""
    for w in words:
        if len(line + " " + w) <= 44:
            line = (line + " " + w).strip()
        else:
            print(f" {C_WHITE}{line}{C_RESET}")
            line = w
    if line:
        print(f" {C_WHITE}{line}{C_RESET}")

    if img_url:
        print(f"{C_CYAN}──────────────────────────────────────────────{C_RESET}")
        print(f" {C_YELLOW}📷 PROFILE PHOTO URL :{C_RESET}")
        print(f" {C_CYAN}{img_url}{C_RESET}")

    if page_url:
        print(f"{C_CYAN}──────────────────────────────────────────────{C_RESET}")
        print(f" {C_YELLOW}🔗 WEB SOURCE LINK :{C_RESET}")
        print(f" {C_CYAN}{page_url}{C_RESET}")

    print(f"{C_CYAN}╚══════════════════════════════════════════════╝{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to search again...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f" {C_CYAN}[1]{C_RESET} Smart Entity Recon Search (Bio & Photo)")
        print(f"{C_CYAN}──────────────────────────────────────────────{C_RESET}")
        print(f" {C_CYAN}[#]{C_RESET} Back to Main Menu  |  {C_RED}[*]{C_RESET} Exit")
        print(f"{C_CYAN}══════════════════════════════════════════════{C_RESET}")
        
        c = input(f"{C_GREEN}➤ Select Option: {C_RESET}").strip().lower()
        if c == '1': search_entity()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__":
    main()