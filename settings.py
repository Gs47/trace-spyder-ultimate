import os, sys, shutil, time, subprocess
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

CACHE_REGISTRY_FILE = os.path.expanduser("~/.trace_spyder_cache_paths.txt")

DEFAULT_CACHE_PATHS = [
    os.path.expanduser("~/.cache"),
    os.path.expanduser("~/../usr/tmp"),
    os.path.expanduser("~/../usr/var/cache/apt/archives"),
    "/sdcard/DCIM/.thumbnails",
    "/sdcard/Pictures/.thumbnails",
    "/sdcard/Android/data/com.android.chrome/cache",
    "/sdcard/Android/data/org.mozilla.firefox/cache"
]

def load_cache_paths():
    if not os.path.exists(CACHE_REGISTRY_FILE):
        save_cache_paths(DEFAULT_CACHE_PATHS)
        return DEFAULT_CACHE_PATHS
    try:
        with open(CACHE_REGISTRY_FILE, "r") as f:
            paths = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        return paths if paths else DEFAULT_CACHE_PATHS
    except:
        return DEFAULT_CACHE_PATHS

def save_cache_paths(paths):
    try:
        with open(CACHE_REGISTRY_FILE, "w") as f:
            f.write("# Trace Spyder Recorded Cache & Internet Junk Paths\n")
            for p in paths:
                f.write(p + "\n")
    except: pass

def get_dir_size(path):
    total_size = 0
    if not os.path.exists(path):
        return 0
    if os.path.isfile(path):
        try: return os.path.getsize(path)
        except: return 0
    try:
        for root, dirs, files in os.walk(path):
            for f in files:
                fp = os.path.join(root, f)
                try: total_size += os.path.getsize(fp)
                except: pass
    except: pass
    return total_size

def format_size(size_bytes):
    if size_bytes == 0: return "0 KB"
    size_name = ("KB", "MB", "GB", "TB")
    i = 0
    s = float(size_bytes) / 1024
    while s >= 1024 and i < len(size_name) - 1:
        s /= 1024
        i += 1
    return f"{round(s, 2)} {size_name[i]}"

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner(sub="TERMUX STORAGE & CACHE CLEANER"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  TRACE SPYDER CLEANER  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'⚡ ═ G O W R I   S H A N K A R ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{f'🚀 ═ {sub} ═ 🚀'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def run_smart_termux_cleanup():
    print_banner("DEEP TERMUX & CACHE CLEANUP")
    print(f"{C_YELLOW}[*] Starting smart safe storage optimization...{C_RESET}\n")
    
    total_freed = 0

    # 1. Clean recorded cache paths
    paths = load_cache_paths()
    for p in paths:
        if os.path.exists(p):
            sz = get_dir_size(p)
            try:
                for root, dirs, files in os.walk(p, topdown=False):
                    for f in files:
                        fp = os.path.join(root, f)
                        try:
                            os.remove(fp)
                        except: pass
                    for d in dirs:
                        dp = os.path.join(root, d)
                        try: os.rmdir(dp)
                        except: pass
                total_freed += sz
                print(f"  {C_GREEN}✔ Cleaned Cache:{C_RESET} {p} ({format_size(sz)})")
            except Exception as e:
                print(f"  {C_RED}✖ Skipped {p}: {e}{C_RESET}")

    # 2. Termux Apt / Pkg cache clean
    print(f"\n{C_YELLOW}[*] Cleaning Termux APT packet archives...{C_RESET}")
    try:
        res = subprocess.run(["pkg", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"  {C_GREEN}✔ pkg clean executed successfully.{C_RESET}")
    except: pass

    # 3. Termux Autoremove orphaned packages (without touching core dependencies)
    print(f"{C_YELLOW}[*] Removing orphaned packages & unused dependencies...{C_RESET}")
    try:
        subprocess.run(["pkg", "autoremove", "-y"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"  {C_GREEN}✔ Orphaned packages purged.{C_RESET}")
    except: pass

    # 4. Python pip cache purge
    print(f"{C_YELLOW}[*] Purging Python pip cache...{C_RESET}")
    try:
        subprocess.run([sys.executable, "-m", "pip", "cache", "purge"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"  {C_GREEN}✔ Python pip cache purged.{C_RESET}")
    except: pass

    print(f"\n{C_GREEN}✅ Smart cleanup complete! Total storage optimized/freed.{C_RESET}")
    input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

def manage_cache_registry():
    while True:
        print_banner("RECORDED CACHE & STORAGE SIZES")
        paths = load_cache_paths()
        print(f"{C_WHITE}Inspecting storage consumption of recorded paths...{C_RESET}\n")
        
        grand_total = 0
        for idx, p in enumerate(paths, 1):
            sz = get_dir_size(p)
            grand_total += sz
            sz_str = format_size(sz)
            
            if sz > 50 * 1024 * 1024:
                size_tag = f"{C_RED}[{sz_str}]{C_RESET}"
            elif sz > 0:
                size_tag = f"{C_YELLOW}[{sz_str}]{C_RESET}"
            else:
                size_tag = f"{C_GREEN}[0 KB]{C_RESET}"
                
            print(f"  {C_CYAN}[{idx}]{C_RESET} {size_tag} {C_WHITE}{p}{C_RESET}")

        print(f"\n{C_MAGENTA}📊 Total Recorded Cache Footprint: {C_GREEN}{format_size(grand_total)}{C_RESET}\n")

        print(f"{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}[1] ➕ Add New Custom Cache / App Path      {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_YELLOW}[2] 🧹 Clean & Wipe All Recorded Caches Now  {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_RED}[3] ❌ Remove a Path from Registry          {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_MAGENTA}[0] 🔙 Back to Settings Menu                {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}")

        ch = input(f"\n{C_GREEN}➤ Select Option (1-3 / 0): {C_RESET}").strip()
        if ch in ['0', 'b', 'back']: break

        if ch == '1':
            print(f"\n{C_WHITE}Enter full folder path to add:{C_RESET}")
            new_p = input(f"{C_GREEN}➤ Path: {C_RESET}").strip()
            if new_p:
                if new_p not in paths:
                    paths.append(new_p)
                    save_cache_paths(paths)
                    print(f"\n{C_GREEN}✔ Successfully added to cache registry!{C_RESET}")
                else:
                    print(f"\n{C_YELLOW}⚠️ Path already exists in registry.{C_RESET}")
                time.sleep(1.2)

        elif ch == '2':
            run_smart_termux_cleanup()

        elif ch == '3':
            rem = input(f"\n{C_GREEN}➤ Enter path number to remove (1-{len(paths)}): {C_RESET}").strip()
            if rem.isdigit():
                r_idx = int(rem) - 1
                if 0 <= r_idx < len(paths):
                    removed = paths.pop(r_idx)
                    save_cache_paths(paths)
                    print(f"\n{C_GREEN}✔ Removed: {removed}{C_RESET}")
                    time.sleep(1.2)

def view_system_diagnostics():
    print_banner("SYSTEM DIAGNOSTICS")
    print(f"{C_WHITE}Gathering device and environment specifications...{C_RESET}\n")
    
    python_ver = sys.version.split()[0]
    termux_prefix = os.environ.get("PREFIX", "/data/data/com.termux/files/usr")
    
    total, used, free = shutil.disk_usage("/sdcard")
    t_gb = round(total / (1024**3), 2)
    u_gb = round(used / (1024**3), 2)
    f_gb = round(free / (1024**3), 2)

    print(f"  {C_CYAN}Python Version    :{C_RESET} {python_ver}")
    print(f"  {C_CYAN}Termux Prefix     :{C_RESET} {termux_prefix}")
    print(f"  {C_CYAN}Storage Total     :{C_RESET} {t_gb} GB")
    print(f"  {C_CYAN}Storage Used      :{C_RESET} {u_gb} GB")
    print(f"  {C_CYAN}Storage Free      :{C_RESET} {f_gb} GB")
    print(f"  {C_CYAN}Cache Registry    :{C_RESET} {CACHE_REGISTRY_FILE}")
    
    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

def main():
    while True:
        print_banner("SYSTEM SETTINGS")
        print(f" {C_CYAN}[1]{C_RESET} 🧹 \033[1mRun Smart Termux & App Cache Deep Cleaner\033[0m")
        print(f" {C_CYAN}[2]{C_RESET} 🗂️  \033[1mManage & Detailed Size Inspection of Cache Paths\033[0m")
        print(f" {C_CYAN}[3]{C_RESET} 📊 \033[1mView System Diagnostics & Storage Info\033[0m")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Option (1-3 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': run_smart_termux_cleanup()
        elif opt == '2': manage_cache_registry()
        elif opt == '3': view_system_diagnostics()

if __name__ == "__main__":
    main()
