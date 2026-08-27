import os, sys, py_compile, subprocess

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
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

ALL_FILES = [
    "menu.py", "ai_chat.py", "media_dl.py", "converter.py", 
    "net_tools.py", "temp_mail.py", "zip_master.py", "qr_tool.py", 
    "file_vault.py", "link_unshort.py", "device_info.py", "phone_cleaner.py", 
    "seeker_hub.py", "recon_tool.py", "crypto_tool.py", "benchmark_tool.py", 
    "hash_tool.py", "encoder_tool.py", "pwgen_tool.py", "web_recon.py", 
    "notes_tool.py", "terabox_dl.py", "search_engine.py", "gmail_bot.py", 
    "settings.py", "about.py"
]

def scan_and_report():
    os.system('clear')
    print(f"{C_CYAN}┌────────────────────────────────────────────────────┐{C_RESET}")
    print(f"{C_WHITE}      🔍 TRACE SPYDER - ERROR DETECTOR & SCANNER    {C_RESET}")
    print(f"{C_CYAN}└────────────────────────────────────────────────────┘{C_RESET}\n")

    broken_files = []
    missing_files = []
    healthy_files = []

    print(f"{C_YELLOW}[*] ഫയലുകൾ ഓരോന്നായി പരിശോധിക്കുന്നു...{C_RESET}\n")

    for fname in ALL_FILES:
        path = os.path.expanduser(f"~/{fname}")
        
        if not os.path.exists(path):
            missing_files.append((fname, "File does not exist"))
            continue
            
        if os.path.getsize(path) == 0:
            broken_files.append((fname, "File is completely empty (0 Bytes)"))
            continue
            
        # സിന്റാക്സ് എറർ പരിശോധന
        try:
            py_compile.compile(path, doraise=True)
            healthy_files.append(fname)
        except py_compile.PyCompileError as e:
            # എറർ വന്ന കൃത്യമായ വരി കണ്ടെത്തുന്നു
            err_line = str(e).splitlines()[-1] if str(e).splitlines() else str(e)
            broken_files.append((fname, err_line[:45]))
        except Exception as e:
            broken_files.append((fname, str(e)[:30]))

    # റിപ്പോർട്ട് കാണിക്കുന്നു
    print(f"{C_GREEN}✔ കൃത്യമായി പ്രവർത്തിക്കുന്നവ ({len(healthy_files)} എണ്ണം):{C_RESET}")
    print(f"  {C_CYAN}{', '.join(healthy_files) if healthy_files else 'None'}{C_RESET}\n")

    if missing_files or broken_files:
        print(f"{C_RED}❌ തകരാർ കണ്ടെത്തിയ ഫയലുകളുടെ പട്ടിക:{C_RESET}")
        print(f"{C_CYAN}────────────────────────────────────────────────────{C_RESET}")
        
        for f, reason in missing_files:
            print(f" {C_RED}✖ [MISSING]{C_RESET} {f:<18} ➔ {C_YELLOW}{reason}{C_RESET}")
            
        for f, reason in broken_files:
            print(f" {C_RED}✖ [BROKEN] {C_RESET} {f:<18} ➔ {C_YELLOW}{reason}{C_RESET}")
            
        print(f"{C_CYAN}────────────────────────────────────────────────────{C_RESET}")
        print(f"\n{C_YELLOW}ആകെ തകരാറുകൾ: {len(missing_files) + len(broken_files)} ഫയലുകൾ.{C_RESET}")
    else:
        print(f"{C_GREEN}🎉 സിസ്റ്റത്തിൽ യാതൊരുവിധ എററുകളോ മിസ്സിംഗ് ഫയലുകളോ ഇല്ല! എല്ലാം 100% പെർഫെക്റ്റാണ്.{C_RESET}")

if __name__ == "__main__":
    scan_and_report()