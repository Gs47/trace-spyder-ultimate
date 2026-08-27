import os, sys, shutil, time, subprocess, glob
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

TORRENT_DIR = "/sdcard/Download/Torrents"

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner(sub="TORRENT DOWNLOADER"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  TORRENT DOWNLOADER  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'⚡ ═ G O W R I   S H A N K A R ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{f'🚀 ═ {sub} ═ 🚀'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def run_aria2(target_source):
    os.makedirs(TORRENT_DIR, exist_ok=True)
    print_banner("DOWNLOADING TORRENT")
    print(f"{C_YELLOW}[*] Destination Folder :{C_RESET} {TORRENT_DIR}")
    print(f"{C_CYAN}[*] Accelerating multi-peer connections...{C_RESET}\n")

    cmd = [
        "aria2c",
        "--dir=" + TORRENT_DIR,
        "--seed-time=0",
        "--max-connection-per-server=16",
        "--min-split-size=1M",
        "--split=16",
        "--enable-dht=true",
        "--enable-peer-exchange=true",
        "--bt-enable-lpd=true",
        "--bt-max-peers=120",
        "--summary-interval=1",
        "--file-allocation=none",
        "--check-certificate=false",
        target_source
    ]

    try:
        subprocess.run(cmd)
        print(f"\n{C_GREEN}✅ Download Complete! Saved in: {TORRENT_DIR}{C_RESET}")
    except KeyboardInterrupt:
        print(f"\n{C_YELLOW}⚠️ Download interrupted by user.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}❌ Error running Aria2 Engine: {e}{C_RESET}")

    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

def download_by_link():
    print_banner("DOWNLOAD VIA LINK / MAGNET")
    print(f"{C_WHITE}Paste your Magnet URL or Direct Web Link (.torrent URL):{C_RESET}\n")
    link = input(f"{C_GREEN}➤ Paste Link: {C_RESET}").strip()
    if not link: return
    if link.startswith("magnet:?") or link.startswith("http://") or link.startswith("https://"):
        run_aria2(link)
    else:
        print(f"\n{C_RED}❌ Invalid link format!{C_RESET}")
        time.sleep(1.2)

def prompt_manual_path():
    print(f"\n{C_RED}╔══════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_RED}║{C_RESET} {C_YELLOW}⌨️  MANUAL PATH ENTRY MODE                  {C_RED}║{C_RESET}")
    print(f"{C_RED}╚══════════════════════════════════════════════╝{C_RESET}")
    print(f"{C_WHITE}Type or paste the exact path to your .torrent file.{C_RESET}")
    print(f"{C_MAGENTA}Example: /storage/emulated/0/Download/file.torrent{C_RESET}\n")
    
    custom_path = input(f"{C_GREEN}➤ Enter Full Path Here: {C_RESET}").strip()
    if custom_path and os.path.exists(custom_path) and os.path.isfile(custom_path):
        run_aria2(custom_path)
    else:
        print(f"\n{C_RED}❌ Error: File does not exist at this path!{C_RESET}")
        input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def download_by_file():
    print_banner("DEEP STORAGE SCAN (.TORRENT)")
    print(f"{C_YELLOW}[*] Performing deep scan across phone storage for .torrent files...{C_RESET}\n")

    torrent_files = []
    search_root = "/sdcard"

    if os.path.exists(search_root):
        for root, dirs, files in os.walk(search_root):
            if "Android/data" in root or "Android/obb" in root:
                continue
            for f in files:
                if f.lower().endswith(".torrent"):
                    torrent_files.append(os.path.join(root, f))

    if not torrent_files:
        print(f"{C_RED}❌ Deep scan could not find any .torrent files automatically.{C_RESET}\n")
        prompt_manual_path()
        return

    print(f"{C_GREEN}✔ Found {len(torrent_files)} .torrent file(s) via deep scan:{C_RESET}\n")
    for idx, tf in enumerate(torrent_files[:25], 1):
        fn = os.path.basename(tf)
        rel_p = tf.replace("/sdcard/", "")
        print(f"  {C_CYAN}[{idx}]{C_RESET} {C_WHITE}{fn[:32]:<34}{C_RESET} {C_YELLOW}(~/{rel_p[:22]}{C_RESET})")

    print(f"\n{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
    print(f"{C_CYAN}│{C_RESET}  {C_MAGENTA}[C] ⌨️  Enter Manual Path Explicitly          {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET}  {C_GREEN}[0] 🔙 Back                                 {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}")

    sel = input(f"\n{C_GREEN}➤ Select Option / File Number: {C_RESET}").strip()
    if sel.lower() in ['c', 'custom']:
        prompt_manual_path()
        return

    if sel.isdigit() and 1 <= int(sel) <= len(torrent_files[:25]):
        chosen_file = torrent_files[int(sel) - 1]
        run_aria2(chosen_file)

def view_downloaded():
    print_banner("DOWNLOADED FILES")
    if not os.path.exists(TORRENT_DIR) or not os.listdir(TORRENT_DIR):
        print(f"\n{C_YELLOW}Torrents folder is empty: {TORRENT_DIR}{C_RESET}")
    else:
        files = os.listdir(TORRENT_DIR)
        print(f"{C_WHITE}Files in {TORRENT_DIR}:{C_RESET}\n")
        for idx, f in enumerate(files[:30], 1):
            fp = os.path.join(TORRENT_DIR, f)
            sz = round(os.path.getsize(fp) / (1024 * 1024), 2) if os.path.isfile(fp) else "DIR"
            print(f"  {C_CYAN}[{idx}]{C_RESET} {C_WHITE}{f[:38]:<40}{C_RESET} {C_GREEN}({sz} MB){C_RESET}")
    input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def main():
    while True:
        print_banner("MAIN OPTIONS")
        print(f" {C_CYAN}[1]{C_RESET} 🔗 \033[1mDownload via Torrent / Magnet Link\033[0m")
        print(f" {C_CYAN}[2]{C_RESET} 📁 \033[1mDownload via .torrent File (Deep Scan & Path)\033[0m")
        print(f" {C_CYAN}[3]{C_RESET} 📂 \033[1mView Downloaded Files\033[0m")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Trace Spyder Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Option (1-3 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': download_by_link()
        elif opt == '2': download_by_file()
        elif opt == '3': view_downloaded()

if __name__ == "__main__":
    main()
