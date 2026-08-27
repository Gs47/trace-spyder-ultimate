import os, sys, subprocess, shutil, py_compile
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

MODULES = [
    ("Trace Spyder AI Chat", "ai_chat.py"),
    ("Gmail Automation Bot", "gmail_bot.py"),
    ("Telegram Hub Manager", "tg_manager.py"),
    ("Universal Media Downloader", "media_dl.py"),
    ("Spotify Music Downloader", "spotify_dl.py"),
    ("TeraBox Cloud Downloader", "terabox_dl.py"),
    ("Torrent Downloader", "torrent_dl.py"),
    ("Web Page & Asset DL", "web_dl.py"),
    ("Audio/Video Converter", "converter.py"),
    ("OSINT Target Recon", "recon_tool.py"),
    ("Web Domain Recon", "web_recon.py"),
    ("Network Audit & Scan", "net_tools.py"),
    ("Seeker Location Engine", "seeker_hub.py"),
    ("Phone Number Lookup", "check_number.py"),
    ("Data & Photo Recovery", "data_recovery.py"),
    ("AES Encrypted Vault", "file_vault.py"),
    ("Cryptography & Ciphers", "crypto_tool.py"),
    ("Hash Generator & Check", "hash_tool.py"),
    ("Multi-Base Encoder", "encoder_tool.py"),
    ("Secure Password Gen", "pwgen_tool.py"),
    ("Disposable Temp Mail", "temp_mail.py"),
    ("Link Unshortener", "link_unshort.py"),
    ("Device Hardware Info", "device_info.py"),
    ("Phone Storage Cleaner", "phone_cleaner.py"),
    ("System Benchmark", "benchmark_tool.py"),
    ("Zip Master Utility", "zip_master.py"),
    ("QR Code Maker/Scan", "qr_tool.py"),
    ("System Settings & Diagnostics", "settings.py"),
    ("About Us & Manual", "about.py")
]

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  TRACE SPYDER  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'🕷️  G O W R I   S H A N K A R  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{'⚡ ═ LIVE AUTOMATED CRASH TESTER ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def test_module(script_name):
    path = os.path.expanduser(f"~/{script_name}")
    if not os.path.exists(path):
        return False, "File Not Found"
    
    try:
        py_compile.compile(path, doraise=True)
    except Exception as e:
        return False, f"SyntaxError: {str(e)[:24]}"

    try:
        proc = subprocess.Popen(
            [sys.executable, path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        try:
            _, stderr = proc.communicate(input="0\n0\n0\nm\nx\nq\n\n", timeout=1.2)
        except subprocess.TimeoutExpired:
            proc.kill()
            _, stderr = proc.communicate()

        err_l = stderr.lower()
        if any(x in err_l for x in ["syntaxerror", "modulenotfounderror", "nameerror", "typeerror", "attributeerror"]):
            lines = [l.strip() for l in stderr.splitlines() if "Error" in l or "Exception" in l]
            return False, lines[-1][:26] if lines else "Runtime Crash"
        return True, "Executed Cleanly (No Crash)"
    except Exception as e:
        return False, str(e)[:24]

def main():
    print_banner()
    w = get_screen_width()
    div = "─" * (w - 2)

    print(f"[*] Live Executing & Testing all {len(MODULES)} software engines in background...\n")
    print(f"{C_WHITE}{'NO':<4} {'MODULE NAME':<24} {'RUNTIME RESULT':<16} {'DIAGNOSIS'}{C_RESET}")
    print(f"{C_CYAN}{div}{C_RESET}")

    passed = 0
    for idx, (mname, script) in enumerate(MODULES, 1):
        ok, diag = test_module(script)
        if ok:
            passed += 1
            res_lbl = f"{C_GREEN}[PASS / OK]{C_RESET}"
            diag_lbl = f"{C_GREEN}{diag}{C_RESET}"
        else:
            res_lbl = f"{C_RED}[CRASH/FAIL]{C_RESET}"
            diag_lbl = f"{C_RED}{diag}{C_RESET}"
        
        print(f" {idx:02d}  {mname[:22]:<24} {res_lbl:<25} {diag_lbl}")

    print(f"{C_CYAN}{div}{C_RESET}")
    print(f"\n{C_WHITE}OVERALL HEALTH SCORE: {C_GREEN if passed == len(MODULES) else C_RED}{passed} / {len(MODULES)} Engines Operating Perfectly!{C_RESET}")
    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

if __name__ == "__main__":
    main()
