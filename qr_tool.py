import os, sys, time, urllib.parse, urllib.request

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_RED = "\033[1;31m"
C_RESET = "\033[0m"

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{C_CYAN}--- QR CODE GENERATOR ---{C_RESET}")
        text = input("\nEnter Text/URL (or 0 to back): ").strip()
        if text in ['0', 'b', 'x', 'm']: break
        if text:
            try:
                res = urllib.request.urlopen(f"https://qrenco.de/{urllib.parse.quote(text)}", timeout=6)
                print("\n" + res.read().decode('utf-8'))
            except Exception as e:
                print(f"{C_RED}ASCII QR Failed: {e}{C_RESET}")
            try:
                path = f"/sdcard/Download/QR_{int(time.time())}.png"
                urllib.request.urlretrieve(f"https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={urllib.parse.quote(text)}", path)
                print(f"{C_GREEN}Saved High-Res PNG to: {path}{C_RESET}")
            except Exception as e:
                print(f"{C_RED}PNG Save Failed: {e}{C_RESET}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
