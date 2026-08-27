import os, sys, subprocess, shutil, glob, time

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

BANNER = """[1;36m┌────────────────────────────────────────────────────────────┐
[1;37m  ████████╗██████╗  █████╗  ██████╗███████╗
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
  ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
[0m
         [1;33m🕷️  [1;36mG O W R I   S H A N K A R[1;33m  🕷️[0m
           [1;35m⚡ ═ [1;32mT E R M I N A L   H U B[1;35m ═ ⚡[0m
[1;36m└────────────────────────────────────────────────────────────┘[0m"""

def get_download_dir():
    if os.name == 'nt':
        return os.path.join(os.path.expanduser("~"), "Downloads")
    if os.path.exists("/sdcard/Download"):
        return "/sdcard/Download"
    return os.path.expanduser("~/Downloads")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(f"{C_MAGENTA}  [▸] ACTIVE MODULE : {C_GREEN}SYSTEM HARDWARE BENCHMARK{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

def run_benchmark():
    clear_screen()
    print(f"{C_YELLOW}[*] Running Multi-threaded Math CPU Stress Test (10,000,000 ops)...{C_RESET}")
    t0 = time.time()
    total = sum(i * i for i in range(10000000))
    t1 = time.time()
    elapsed = max(0.001, t1 - t0)
    score = int(10000 / elapsed)
    
    print(f"\n{C_CYAN}╔═════════════════════ [ BENCHMARK RESULTS ] ═════════════════════╗{C_RESET}")
    print(f"  {C_GREEN}Execution Time :{C_RESET} {C_WHITE}{elapsed:.3f} Seconds{C_RESET}")
    print(f"  {C_GREEN}Performance Score:{C_RESET} {C_YELLOW}{score} Pts{C_RESET}")
    print(f"  {C_GREEN}Hardware Rating:{C_RESET} {C_WHITE}{'Exceptional' if score > 8000 else 'Balanced / Standard'}{C_RESET}")
    print(f"{C_CYAN}╚═════════════════════════════════════════════════════════════════╝{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Run Instant CPU & Arithmetic Benchmark")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Select Option (1): {C_RESET}").strip().lower()
        if c == '1': run_benchmark()
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
