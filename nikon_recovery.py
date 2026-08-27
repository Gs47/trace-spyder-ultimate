import os, sys, shutil, time, glob
from datetime import datetime

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_RESET = "\033[0m"

RESTORE_DIR = "/sdcard/Download/Nikon_Recovered"
os.makedirs(RESTORE_DIR, exist_ok=True)

# Nikon JPEG and Nikon RAW (.NEF / TIFF) Magic Bytes
SIGS = {
    b"\xFF\xD8\xFF": "jpg",
    b"\x49\x49\x2A\x00": "nef", # Nikon RAW Little Endian
    b"\x4D\x4D\x00\x2A": "nef"  # Nikon RAW Big Endian
}

def scan_path(target):
    print(f"\n{C_YELLOW}[*] Deep Scanning: {target}{C_RESET}")
    found = 0
    for root, _, files in os.walk(target):
        for f in files:
            fp = os.path.join(root, f)
            try:
                sz = os.path.getsize(fp)
                if sz > 20 * 1024: # Filter > 20KB
                    with open(fp, "rb") as rf:
                        head = rf.read(16)
                    
                    ext = None
                    for sig, ext_name in SIGS.items():
                        if head.startswith(sig):
                            ext = ext_name
                            break
                    
                    if ext:
                        mtime = os.path.getmtime(fp)
                        d_str = datetime.fromtimestamp(mtime).strftime("%Y%m%d_%H%M%S")
                        dest = os.path.join(RESTORE_DIR, f"Nikon_{d_str}_{found:04d}.{ext}")
                        shutil.copy2(fp, dest)
                        found += 1
                        print(f"  {C_GREEN}✔ Resurrected:{C_RESET} {os.path.basename(dest)} ({round(sz/(1024*1024), 2)} MB)")
            except Exception: pass
    print(f"{C_GREEN}Done. Found {found} files from this path.{C_RESET}")

def main():
    os.system('clear')
    print(f"{C_CYAN}=== NIKON D5000 FORENSIC RECOVERY ENGINE ==={C_RESET}\n")
    print("1. Scan Entire Phone Internal Cache (Extract Gallery copies)")
    print("2. Enter Custom SD Card Path (e.g. /storage/62B3-1814)")
    print("0. Exit")
    
    ch = input(f"\n{C_GREEN}Select Option: {C_RESET}").strip()
    if ch == '1':
        for p in ["/sdcard/DCIM", "/sdcard/Pictures", "/sdcard/Android/media", "/sdcard/LOST.DIR"]:
            if os.path.exists(p): scan_path(p)
    elif ch == '2':
        p = input("Enter Path: ").strip()
        if os.path.exists(p): scan_path(p)
        else: print(f"{C_RED}Path not found.{C_RESET}")
    
    print(f"\n{C_CYAN}Check recovered files in:{C_RESET} {RESTORE_DIR}")

if __name__ == "__main__":
    main()
