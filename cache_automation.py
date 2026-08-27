import os, sys, subprocess, time

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


def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode('utf-8').strip()
    except Exception:
        return ""

def run_nothing_os_cache_wiper():
    print("\n" + "="*52)
    print("      NOTHING OS AUTO-UI CACHE WIPER ENGINE       ")
    print("="*52)
    
    check_adb = run_cmd("adb devices")
    if "127.0.0.1" not in check_adb and "device" not in check_adb:
        print("❌ ADB not connected! Connect Wireless ADB first.")
        return

    # Screen resolution detection
    wm_size = run_cmd("adb shell wm size")
    width, height = 1080, 2400
    if "Physical size:" in wm_size:
        try:
            sz = wm_size.split("Physical size:")[1].strip().split("x")
            width, height = int(sz[0]), int(sz[1])
        except Exception:
            pass

    # --- Nothing OS Layout Calculations ---
    # 1. 'Storage & cache' menu position on App Info page
    storage_cache_x = int(width * 0.50)
    storage_cache_y = int(height * 0.42)
    
    # 2. 'Clear cache' button on Storage page (Right side pill button)
    clear_cache_btn_x = int(width * 0.74)
    clear_cache_btn_y = int(height * 0.23)

    print(f"[*] Display Profile : {width}x{height} (Nothing OS Calibration)")
    print("[*] Fetching installed 3rd-party apps...")
    
    pkgs = run_cmd("adb shell pm list packages -3").splitlines()
    packages = [p.replace("package:", "").strip() for p in pkgs if p.strip()]
    
    print(f"[*] Detected {len(packages)} installed applications.")
    print("⚠️ KEEP PHONE SCREEN UNLOCKED while running automation.\n")
    
    confirm = input("Start clearing caches now? (y/n): ").strip().lower()
    if confirm != 'y': return

    print("\n🚀 Starting Nothing OS cache purge loop...\n")
    count = 0
    for pkg in packages:
        count += 1
        print(f"[{count}/{len(packages)}] Purging cache: {pkg}")
        
        # Step 1: Open App Info page
        run_cmd(f"adb shell am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:{pkg}")
        time.sleep(0.9)
        
        # Step 2: Tap 'Storage & cache'
        run_cmd(f"adb shell input tap {storage_cache_x} {storage_cache_y}")
        time.sleep(0.7)
        
        # Step 3: Tap 'Clear cache'
        run_cmd(f"adb shell input tap {clear_cache_btn_x} {clear_cache_btn_y}")
        time.sleep(0.5)
        
        # Step 4: Back out to clean state
        run_cmd("adb shell input keyevent 4")
        time.sleep(0.2)
        run_cmd("adb shell input keyevent 4")
        time.sleep(0.2)

    # Return to Termux
    run_cmd("adb shell monkey -p com.termux 1")
    print("\n" + "="*52)
    print(f"✅ Finished cache purge across all {len(packages)} apps!")
    print("="*52)

def main():
    while True:
        print("\n" + "="*52)
        print("       NOTHING OS TERMINAL CACHE PURGE HUB       ")
        print("="*52)
        print("[1] Start Nothing OS Automated Cache Wiper")
        print("[2] Check ADB Connection Status")
        print("--------------------------------------------------")
        print("[0]  Refresh / Stay Here")
        print("[99] Return to Main Menu Hub")
        print("="*52)
        
        c = input("Select Option (1-2 / 99): ").strip()
        if c == '1':
            run_nothing_os_cache_wiper()
            input("\nPress Enter to return...")
        elif c == '2':
            out = run_cmd("adb devices")
            print("\n--- Active ADB Status ---")
            print(out if out else "No active device.")
            input("\nPress Enter to return...")
        elif c == '0':
            continue
        elif c in ['99', 'q', 'exit']:
            break

if __name__ == "__main__":
    main()