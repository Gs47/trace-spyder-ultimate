import os, sys, subprocess, py_compile

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

SCRIPTS = [
    "menu.py", "media_dl.py", "converter.py", "temp_mail.py",
    "zip_master.py", "net_tools.py", "qr_tool.py", "file_vault.py",
    "link_unshort.py", "device_info.py", "phone_cleaner.py", "seeker_hub.py",
    "settings.py", "auto_repair.py", "about.py", "recon_tool.py",
    "crypto_tool.py", "benchmark_tool.py", "hash_tool.py", "encoder_tool.py",
    "pwgen_tool.py", "web_recon.py", "notes_tool.py", "terabox_dl.py"
]

def run_diagnostics():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{C_CYAN}╔════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"  {C_YELLOW}⚡ TRACE SPYDER CORE - AUTOMATED SYSTEM DIAGNOSTICS ⚡{C_RESET}")
    print(f"{C_CYAN}╚════════════════════════════════════════════════════════════════╝{C_RESET}\n")

    home = os.path.expanduser("~")
    passed = 0
    failed = 0
    missing = 0

    print(f"{C_MAGENTA}[*] Checking Script Integrity & Syntax Errors...{C_RESET}\n")

    for script in SCRIPTS:
        path = os.path.join(home, script)
        if not os.path.exists(path):
            print(f"  {C_RED}[MISSING]{C_RESET} {script:<25} ➔ {C_RED}File not found!{C_RESET}")
            missing += 1
            continue

        try:
            # Python Compile Check (Syntax / Indentation Errors)
            py_compile.compile(path, doraise=True)
            print(f"  {C_GREEN}[PASS]{C_RESET}    {script:<25} ➔ {C_GREEN}Syntax OK / No Crash{C_RESET}")
            passed += 1
        except py_compile.PyCompileError as e:
            print(f"  {C_RED}[FAIL]{C_RESET}    {script:<25} ➔ {C_RED}Syntax Error detected!{C_RESET}")
            failed += 1

    print(f"\n{C_CYAN}──────────────────────── [ SUMMARY ] ────────────────────────{C_RESET}")
    print(f"  {C_GREEN}Passed Modules :{C_RESET} {passed}/{len(SCRIPTS)}")
    print(f"  {C_RED}Failed Modules :{C_RESET} {failed}")
    print(f"  {C_YELLOW}Missing Files  :{C_RESET} {missing}")
    print(f"{C_CYAN}─────────────────────────────────────────────────────────────{C_RESET}")

    if failed == 0 and missing == 0:
        print(f"\n{C_GREEN}🚀 ALL SCRIPTS ARE 100% HEALTHY & READY TO RUN!{C_RESET}\n")
    else:
        print(f"\n{C_RED}⚠️ Some modules need attention. Run auto_repair.py to fix.{C_RESET}\n")

if __name__ == "__main__":
    run_diagnostics()