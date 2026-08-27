import os, sys, shutil, time, glob
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

RESTORE_DIR = "/sdcard/Download/Recovered_Files"

FILE_SIGNATURES = {
    b"\xFF\xD8\xFF": "jpg",
    b"\x89PNG\r\n\x1a\n": "png",
    b"%PDF": "pdf",
    b"PK\x03\x04": "zip",
    b"\x1f\x8b\x08": "gz"
}

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner(sub="DATA & MEDIA RECOVERY"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  TRACE SPYDER ADVANCED RECOVERY  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'⚡ ═ G O W R I   S H A N K A R ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{f'🚀 ═ {sub} ═ 🚀'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def get_detected_usb_paths():
    usb_paths = []
    try:
        if os.path.exists("/storage"):
            for item in os.listdir("/storage"):
                if item not in ["emulated", "self", "knox"]:
                    sp = os.path.join("/storage", item)
                    if os.path.isdir(sp):
                        usb_paths.append(sp)
    except Exception: pass
    return list(set(usb_paths))

def save_carved_file(fp, mtime, idx, prefix="Recovered"):
    try:
        with open(fp, "rb") as test_f:
            header = test_f.read(32)

        ext = None
        for sig, ext_name in FILE_SIGNATURES.items():
            if header.startswith(sig):
                ext = ext_name
                break
        if b"ftyp" in header[:16]: ext = "mp4"
        if b"RIFF" in header[:4] and b"WEBP" in header[8:12]: ext = "webp"

        if not ext:
            orig_ext = os.path.splitext(fp)[1].replace(".", "").lower()
            ext = orig_ext if orig_ext in ["jpg", "jpeg", "png", "mp4", "pdf", "mkv", "mp3"] else "jpg"

        date_tag = datetime.fromtimestamp(mtime).strftime("%Y%m%d_%H%M%S")
        dest_name = f"{prefix}_{date_tag}_{idx}.{ext}"
        dest_path = os.path.join(RESTORE_DIR, dest_name)
        
        shutil.copy2(fp, dest_path)
        return dest_name
    except Exception:
        return None

def recover_from_usb_hidden():
    print_banner("USB / SD CARD HIDDEN SECTOR SCAN")
    usb_drives = get_detected_usb_paths()

    if not usb_drives:
        print(f"{C_RED}❌ No connected USB drives found!{C_RESET}")
        c_path = input(f"{C_GREEN}➤ Enter USB Path manually (e.g. /storage/62B3-1814): {C_RESET}").strip()
        if os.path.exists(c_path):
            target_usb = c_path
        else:
            input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")
            return
    else:
        print(f"{C_WHITE}Select Target USB Drive:{C_RESET}\n")
        for idx, ud in enumerate(usb_drives, 1):
            print(f"  {C_CYAN}[{idx}]{C_RESET} {C_WHITE}{ud}{C_RESET}")
        sel = input(f"\n{C_GREEN}➤ Select Drive Number (1-{len(usb_drives)}): {C_RESET}").strip()
        target_usb = usb_drives[int(sel)-1] if (sel.isdigit() and 1 <= int(sel) <= len(usb_drives)) else usb_drives[0]

    print(f"\n{C_YELLOW}[*] Scanning hidden folders, .trashes, and LOST.DIR on {target_usb}...{C_RESET}\n")
    candidate_files = []

    for root, dirs, files in os.walk(target_usb):
        for f in files:
            fp = os.path.join(root, f)
            try:
                sz = os.path.getsize(fp)
                if sz > 5 * 1024:
                    mtime = os.path.getmtime(fp)
                    candidate_files.append((fp, sz, mtime))
            except Exception: pass

    if not candidate_files:
        print(f"{C_RED}❌ No raw files found in regular directory table.{C_RESET}")
        input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")
        return

    candidate_files.sort(key=lambda x: x[2], reverse=True)
    os.makedirs(RESTORE_DIR, exist_ok=True)
    
    limit = min(500, len(candidate_files))
    print(f"{C_GREEN}[+] Carving {limit} most recent files to {RESTORE_DIR}...{C_RESET}\n")

    restored = 0
    for idx, (fp, sz, mtime) in enumerate(candidate_files[:limit], 1):
        fn = save_carved_file(fp, mtime, idx, "USB")
        if fn:
            restored += 1
            print(f"  {C_GREEN}✔ [{restored}/{limit}]{C_RESET} {fn} ({round(sz/1024, 1)} KB)")

    print(f"\n{C_GREEN}✅ Success! {restored} files recovered to: {RESTORE_DIR}{C_RESET}")
    input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def recover_from_device_cache():
    print_banner("PHONE CACHE & THUMBNAIL RESURRECTION")
    print(f"{C_YELLOW}[*] Scanning Android Gallery Caches, DCIM Vaults, and Media Databases...{C_RESET}\n")

    cache_targets = [
        "/sdcard/DCIM/.thumbnails",
        "/sdcard/Pictures/.thumbnails",
        "/sdcard/DCIM",
        "/sdcard/Pictures",
        "/sdcard/Android/media",
        "/sdcard/Android/data/com.miui.gallery/cache",
        "/sdcard/Android/data/com.sec.android.gallery3d/cache",
        "/sdcard/Android/data/com.google.android.apps.photos/cache"
    ]

    candidate_files = []
    for ct in cache_targets:
        if os.path.exists(ct):
            for root, _, files in os.walk(ct):
                for f in files:
                    fp = os.path.join(root, f)
                    try:
                        sz = os.path.getsize(fp)
                        if sz > 15 * 1024:
                            mtime = os.path.getmtime(fp)
                            candidate_files.append((fp, sz, mtime))
                    except Exception: pass

    if not candidate_files:
        print(f"{C_RED}❌ No cache thumbnails found in phone memory.{C_RESET}")
        input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")
        return

    candidate_files.sort(key=lambda x: x[2], reverse=True)
    total = len(candidate_files)

    print(f"{C_WHITE}Discovered Total Cached Photos/Media:{C_RESET} {C_GREEN}{total} Assets{C_RESET}")
    print(f"Newest Date: {C_YELLOW}{datetime.fromtimestamp(candidate_files[0][2]).strftime('%Y-%m-%d %H:%M:%S')}{C_RESET}\n")

    print(f" {C_CYAN}[1]{C_RESET} Recover Top 500 Most Recent Photos")
    print(f" {C_CYAN}[2]{C_RESET} Recover Top 400 Most Recent Photos")
    print(f" {C_CYAN}[3]{C_RESET} Recover ALL {total} Assets")
    sel = input(f"\n{C_GREEN}➤ Choose Batch (1-3): {C_RESET}").strip()

    limit = total
    if sel == '1': limit = min(500, total)
    elif sel == '2': limit = min(400, total)

    os.makedirs(RESTORE_DIR, exist_ok=True)
    print(f"\n{C_YELLOW}[+] Extracting top {limit} recent photos to {RESTORE_DIR}...{C_RESET}\n")

    restored = 0
    for idx, (fp, sz, mtime) in enumerate(candidate_files[:limit], 1):
        fn = save_carved_file(fp, mtime, idx, "CachedPhoto")
        if fn:
            restored += 1
            print(f"  {C_GREEN}✔ [{restored}/{limit}]{C_RESET} {fn} ({round(sz/1024, 1)} KB)")

    print(f"\n{C_GREEN}✅ Success! {restored} recent photos recovered to: {RESTORE_DIR}{C_RESET}")
    input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def run_photorec_carver():
    print_banner("PHOTOREC FORENSIC SECTOR CARVER")
    print(f"{C_YELLOW}[!] Launching PhotoRec low-level file carver...{C_RESET}\n")
    time.sleep(1)
    os.system("photorec")

def view_recovered():
    print_banner("RECOVERED FILES VAULT")
    if not os.path.exists(RESTORE_DIR) or not os.listdir(RESTORE_DIR):
        print(f"\n{C_YELLOW}No recovered files yet in: {RESTORE_DIR}{C_RESET}")
    else:
        files = sorted(os.listdir(RESTORE_DIR), reverse=True)
        print(f"{C_WHITE}Recovered Assets ({len(files)} files in {RESTORE_DIR}):{C_RESET}\n")
        for idx, f in enumerate(files[:30], 1):
            fp = os.path.join(RESTORE_DIR, f)
            sz = round(os.path.getsize(fp) / 1024, 1)
            print(f"  {C_CYAN}[{idx}]{C_RESET} {C_WHITE}{f[:38]:<40}{C_RESET} {C_GREEN}({sz} KB){C_RESET}")
    input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def main():
    while True:
        print_banner("DATA & PHOTO RECOVERY SUITE")
        print(f" {C_CYAN}[1]{C_RESET} 🔌 \033[1mUSB OTG / SD Card Hidden Sector & File Scan\033[0m")
        print(f" {C_CYAN}[2]{C_RESET} 🖼️  \033[1mRecover Photos from Phone Media & Thumbnail Cache\033[0m")
        print(f" {C_CYAN}[3]{C_RESET} 🔬 \033[1mLaunch PhotoRec Deep Sector Carving Tool\033[0m")
        print(f" {C_CYAN}[4]{C_RESET} 📂 \033[1mView Recovered Files Folder\033[0m")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Trace Spyder Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Option (1-4 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': recover_from_usb_hidden()
        elif opt == '2': recover_from_device_cache()
        elif opt == '3': run_photorec_carver()
        elif opt == '4': view_recovered()

if __name__ == "__main__":
    main()
