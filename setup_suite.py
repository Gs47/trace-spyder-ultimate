import os, sys, shutil

print("[*] Building Trace Spyder Modular 600+ Architecture...")

BASE_DIR = os.path.expanduser("~")
MODULES_DIR = os.path.join(BASE_DIR, "modules")

CATEGORIES = {
    "1": ("📥 MEDIA & DOWNLOADERS", "media"),
    "2": ("🌐 NETWORKING & SCANNERS", "network"),
    "3": ("🔒 SECURITY & CRYPTO VAULT", "security"),
    "4": ("🕵️ OSINT & INTELLIGENCE", "recon"),
    "5": ("⚙️ SYSTEM & STORAGE TOOLS", "system"),
    "6": ("💻 DEVELOPER & UTILITIES", "utils")
}

# Create category folders
for _, folder in CATEGORIES.values():
    os.makedirs(os.path.join(MODULES_DIR, folder), exist_ok=True)

# -----------------------------------------------------------------
# DYNAMIC CATEGORIZED MENU.PY
# -----------------------------------------------------------------
menu_code = r'''import os, sys, shutil, subprocess
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

MODULES_DIR = os.path.expanduser("~/modules")

CATEGORIES = {
    "1": ("📥 MEDIA & DOWNLOADERS", "media"),
    "2": ("🌐 NETWORKING & SCANNERS", "network"),
    "3": ("🔒 SECURITY & CRYPTO VAULT", "security"),
    "4": ("🕵️ OSINT & INTELLIGENCE", "recon"),
    "5": ("⚙️ SYSTEM & STORAGE TOOLS", "system"),
    "6": ("💻 DEVELOPER & UTILITIES", "utils")
}

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    bar = "─" * (w - 2)
    print(f"{C_CYAN}┌{bar}┐{C_RESET}")
    print(f"""{C_WHITE}  ████████╗██████╗  █████╗  ██████╗███████╗
  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
     ██║   ██████╔╝███████║██║     █████╗  
     ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
     ██║   ██║  ██║██║  ██║╚██████╗███████╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝

  ███████╗██████╗ ██╗   ██╗██████╗ ███████╗██████╗ 
  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
  ███████╗██████╔╝ ╚████╔╝ ██║  ██║█████╗  ██████╔╝
  ╚════██║██╔═══╝   ╚██╔╝  ██║  ██║██╔══╝  ██╔══██╗
  ███████║██║        ██║   ██████╔╝███████╗██║  ██║
  ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝{C_RESET}
         {C_YELLOW}🕷️  {C_CYAN}G O W R I   S H A N K A R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}MODULAR 600+ SUITE{C_MAGENTA} ═ ⚡{C_RESET}""")
    print(f"{C_CYAN}└{bar}┘{C_RESET}")

def run_tool(filepath):
    if os.path.exists(filepath):
        proc = subprocess.run([sys.executable, filepath])
        if proc.returncode == 99:
            sys.exit(0)
    else:
        print(f"\n{C_RED}❌ Module path not found.{C_RESET}")
        time.sleep(1)

def open_category_menu(cat_name, folder_name):
    cat_path = os.path.join(MODULES_DIR, folder_name)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print(f"\n{C_YELLOW}📂 CATEGORY: {cat_name}{C_RESET}\n")
        
        if not os.path.exists(cat_path):
            os.makedirs(cat_path, exist_ok=True)
            
        py_files = sorted([f for f in os.listdir(cat_path) if f.endswith('.py')])
        
        if not py_files:
            print(f"  {C_RED}No tools found in this category yet.{C_RESET}")
            print(f"  {C_WHITE}Drop .py plugins into ~/modules/{folder_name}/{C_RESET}")
        else:
            for idx, fname in enumerate(py_files, 1):
                clean_name = fname.replace('.py', '').replace('_', ' ').upper()
                print(f"  {C_CYAN}[{idx:02d}]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}\033[1m{clean_name}\033[0m")

        print(f"\n{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}[0] 🔙 Back to Main Menu                  {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}")

        raw = input(f"\n{C_GREEN}➤ Select Tool Number: {C_RESET}").strip()
        if raw in ['0', 'b', 'back']: break
        
        if raw.isdigit():
            i = int(raw) - 1
            if 0 <= i < len(py_files):
                run_tool(os.path.join(cat_path, py_files[i]))

def main():
    while True:
        w = get_screen_width()
        bar = "─" * (w - 2)
        print_banner()

        print(f"\n{C_YELLOW}╔{'═' * (w-2)}╗{C_RESET}")
        print(f"{C_YELLOW}║{C_RESET} {C_RED}[*]{C_GREEN} \033[1m🤖 TRACE SPYDER AI CHAT (NEURAL CORE) ⚡\033[0m {C_YELLOW}║{C_RESET}")
        print(f"{C_YELLOW}╚{'═' * (w-2)}╝{C_RESET}\n")

        # Display Categories (Scalable up to 600+ tools across folders)
        for k, (cat_label, _) in CATEGORIES.items():
            print(f"  {C_CYAN}[{k}]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}\033[1m{cat_label}\033[0m")

        print(f"\n{C_CYAN}┌{bar}┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}\033[1m[7] ⚙️  SYSTEM SETTINGS & DIAGNOSTICS\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_MAGENTA}\033[1m[8] 📖 COMPLETE MANUAL & ABOUT US\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_RED}\033[1m[0/x] 🚪 EXIT TERMINAL / CLOSE SESSION\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└{bar}┘{C_RESET}")

        raw = input(f"\n{C_GREEN}➤ Select Category (1-8 / [0/x] Exit): {C_RESET}").strip().lower()

        if raw in ['*', '@', 'ai']:
            run_tool(os.path.expanduser("~/ai_chat.py"))
            continue

        if raw in ['0', '00', 'x', 'exit', 'q', 'quit']:
            print(f"\n{C_YELLOW}Closing Trace Spyder Terminal. Goodbye!{C_RESET}\n")
            sys.exit(0)

        if raw == '7':
            run_tool(os.path.expanduser("~/settings.py"))
        elif raw == '8':
            run_tool(os.path.expanduser("~/about.py"))
        elif raw in CATEGORIES:
            label, folder = CATEGORIES[raw]
            open_category_menu(label, folder)

if __name__ == "__main__":
    main()
'''

with open(os.path.expanduser("~/menu.py"), "w") as f:
    f.write(menu_code)

print("[+] Modular Dynamic Menu generated successfully!")
