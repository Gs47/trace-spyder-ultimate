import os, sys, urllib.request

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_RED = "\033[1;31m"
C_RESET = "\033[0m"

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{C_CYAN}--- LINK UNSHORTENER ---{C_RESET}")
        url = input("\nEnter Short URL (or 0 to back): ").strip()
        if url in ['0', 'b', 'x', 'm']: break
        if url:
            if not url.startswith("http"): url = "http://" + url
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                res = urllib.request.urlopen(req, timeout=8)
                print(f"\n{C_GREEN}Final URL: {res.geturl()}{C_RESET}")
            except Exception as e:
                print(f"{C_RED}Failed: {e}{C_RESET}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
