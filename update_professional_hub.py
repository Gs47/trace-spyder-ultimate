import os

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


BANNER = """\033[1;36m┌────────────────────────────────────────────────────────────┐
\033[1;37m  ████████╗██████╗  █████╗  ██████╗███████╗
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
\033[0m
         \033[1;33m🕷️  \033[1;36mG O W R I   S H A N K A R\033[1;33m  🕷️\033[0m
           \033[1;35m⚡ ═ \033[1;32mT E R M I N A L   H U B\033[1;35m ═ ⚡\033[0m
\033[1;36m└────────────────────────────────────────────────────────────┘\033[0m"""

def get_header(title):
    return f'''import os, sys, subprocess, shutil, glob

C_CYAN = "\\033[1;36m"
C_GREEN = "\\033[1;32m"
C_YELLOW = "\\033[1;33m"
C_RED = "\\033[1;31m"
C_MAGENTA = "\\033[1;35m"
C_WHITE = "\\033[1;37m"
C_RESET = "\\033[0m"

BANNER = """{BANNER}"""

def get_download_dir():
    if os.name == 'nt':
        return os.path.join(os.path.expanduser("~"), "Downloads")
    if os.path.exists("/sdcard/Download"):
        return "/sdcard/Download"
    return os.path.expanduser("~/Downloads")

def get_music_dir():
    if os.name == 'nt':
        return os.path.join(os.path.expanduser("~"), "Music")
    if os.path.exists("/sdcard/Music"):
        return "/sdcard/Music"
    return os.path.expanduser("~/Music")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(f"{{C_MAGENTA}}  [▸] ACTIVE MODULE : {{C_GREEN}}{title}{{C_RESET}}")
    print(f"{{C_CYAN}}─"*60 + f"{{C_RESET}}")
'''

# 1. Main Menu (Strict A-Z Sorted)
menu_code = get_header("MAIN DASHBOARD (A-Z ENGINE)") + '''
def run_script(script_name):
    path = os.path.expanduser(f"~/{script_name}")
    if os.path.exists(path):
        subprocess.run([sys.executable, path])
    else:
        print(f"\\n{C_RED}❌ Error: {script_name} not found!{C_RESET}")
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET}  Archive & ZIP Master Engine (Create / Extract / Unlock)")
        print(f"  {C_CYAN}[2]{C_RESET}  Device & Battery Diagnostic Status")
        print(f"  {C_CYAN}[3]{C_RESET}  Media & Document Converter Engine (FFmpeg & Images)")
        print(f"  {C_CYAN}[4]{C_RESET}  Seeker OSINT Location Explorer")
        print(f"  {C_CYAN}[5]{C_RESET}  Settings & Core Engine Updater")
        print(f"  {C_CYAN}[6]{C_RESET}  Spotify Smart Music & Video Downloader")
        print(f"  {C_CYAN}[7]{C_RESET}  System Auto-Repair & Diagnostic Engine")
        print(f"  {C_CYAN}[8]{C_RESET}  Telegram Cloud Hub (Multi-Account / File Sync)")
        print(f"  {C_CYAN}[9]{C_RESET}  Temporary Disposable Email & Live Inbox")
        print(f"  {C_CYAN}[10]{C_RESET} TeraBox Fast Video Downloader")
        print(f"  {C_CYAN}[11]{C_RESET} Termux Storage & Cache Purger")
        print(f"  {C_CYAN}[12]{C_RESET} Universal Media Downloader (YT/IG/FB/X/etc)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_YELLOW}[0]{C_RESET}  Refresh Dashboard")
        print(f"  {C_RED}[*]{C_RESET}  Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        
        choice = input(f"{C_GREEN}➤ Select Module (1-12): {C_RESET}").strip().lower()
        mapping = {
            '1': 'zip_master.py', '01': 'zip_master.py',
            '2': 'device_info.py', '02': 'device_info.py',
            '3': 'converter.py', '03': 'converter.py',
            '4': 'seeker_hub.py', '04': 'seeker_hub.py',
            '5': 'settings.py', '05': 'settings.py',
            '6': 'spotify_dl.py', '06': 'spotify_dl.py',
            '7': 'auto_repair.py', '07': 'auto_repair.py',
            '8': 'tools.py', '08': 'tools.py',
            '9': 'temp_mail.py', '09': 'temp_mail.py',
            '10': 'terabox_dl.py',
            '11': 'phone_cleaner.py',
            '12': 'media_dl.py'
        }
        if choice in mapping:
            run_script(mapping[choice])
        elif choice == '0':
            continue
        elif choice in ['*', 'x', 'exit', 'q']:
            print(f"\\n{C_RED}Exiting Trace Spyder Hub. Goodbye!{C_RESET}\\n")
            sys.exit(0)
        else:
            input(f"\\n{C_RED}❌ Invalid selection! Press Enter...{C_RESET}")

if __name__ == "__main__":
    main_menu()
'''

# 2. Media Downloader (A-Z Sorted)
media_dl_code = get_header("UNIVERSAL MEDIA DOWNLOADER") + '''
def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Facebook Video Downloader")
        print(f"  {C_CYAN}[2]{C_RESET} Instagram Reels / Post / Story")
        print(f"  {C_CYAN}[3]{C_RESET} TeraBox Fast Video Downloader")
        print(f"  {C_CYAN}[4]{C_RESET} Universal Stream Downloader (TikTok / X / Others)")
        print(f"  {C_CYAN}[5]{C_RESET} YouTube Video / Shorts / Playlist")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        choice = input(f"{C_GREEN}➤ Select Platform (1-5): {C_RESET}").strip().lower()
        if choice in ['#', 'b', 'back']: break
        elif choice in ['*', 'x', 'exit', 'q']: sys.exit(0)

        platform_map = {'1': 'Facebook', '2': 'Instagram', '3': 'TeraBox', '4': 'Universal', '5': 'YouTube'}
        if choice in platform_map:
            p_name = platform_map[choice]
            clear_screen()
            print(f"{C_YELLOW}[*] Selected Platform: {C_CYAN}{p_name} Downloader{C_RESET}\\n")
            url = input(f"{C_GREEN}➤ Paste {p_name} URL ([#] Back / [*] Exit): {C_RESET}").strip()
            if url.lower() in ['#', 'b', 'back']: continue
            elif url.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
            elif url:
                out_dir = get_download_dir()
                os.makedirs(out_dir, exist_ok=True)
                print(f"\\n{C_YELLOW}[*] Downloading into {out_dir}...{C_RESET}")
                subprocess.run(["yt-dlp", "-P", out_dir, url])
                input(f"\\n{C_GREEN}✅ Finished. Press Enter...{C_RESET}")
        else:
            input(f"\\n{C_RED}❌ Invalid option! Press Enter...{C_RESET}")

if __name__ == "__main__": main()
'''

# 3. Converter Hub (A-Z Sorted)
converter_code = get_header("FAST MEDIA & DOC CONVERTER") + '''
from PIL import Image

def get_input_path(prompt_text):
    path = input(f"{C_GREEN}➤ {prompt_text} ([#] Back / [*] Exit): {C_RESET}").strip().strip("\'\\"")
    if path.lower() in ['#', 'b', 'back']: return None
    elif path.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
    if not os.path.exists(path):
        print(f"\\n{C_RED}❌ Error: File not found!{C_RESET}")
        input("Press Enter...")
        return False
    return path

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Audio Format Conversion (WAV/AAC/OGG to MP3)")
        print(f"  {C_CYAN}[2]{C_RESET} Compress Video (Reduce File Size)")
        print(f"  {C_CYAN}[3]{C_RESET} Image Format Switcher (JPG ⇆ PNG ⇆ WEBP)")
        print(f"  {C_CYAN}[4]{C_RESET} Images (JPG/PNG) to PDF Document")
        print(f"  {C_CYAN}[5]{C_RESET} PDF Document to Images (PNG/JPG Pages)")
        print(f"  {C_CYAN}[6]{C_RESET} Video Format Conversion (MKV/AVI/WEBM to MP4)")
        print(f"  {C_CYAN}[7]{C_RESET} Video to Animated GIF")
        print(f"  {C_CYAN}[8]{C_RESET} Video to MP3 Audio (320kbps Crystal Clear)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        c = input(f"{C_GREEN}➤ Select Option (1-8): {C_RESET}").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)
        elif c in ['1', '2', '6', '7', '8']:
            p = get_input_path("Enter Media File Path")
            if not p: continue
            base = os.path.splitext(p)[0]
            cmd = []
            if c == '1': cmd = ["ffmpeg", "-i", p, "-ab", "320k", base + "_converted.mp3", "-y"]
            elif c == '2': cmd = ["ffmpeg", "-i", p, "-vcodec", "libx264", "-crf", "28", base + "_compressed.mp4", "-y"]
            elif c == '6': cmd = ["ffmpeg", "-i", p, "-c:v", "libx264", "-c:a", "aac", base + "_converted.mp4", "-y"]
            elif c == '7': cmd = ["ffmpeg", "-i", p, "-vf", "fps=10,scale=320:-1:flags=lanczos", base + ".gif", "-y"]
            elif c == '8': cmd = ["ffmpeg", "-i", p, "-vn", "-ab", "320k", base + ".mp3", "-y"]
            subprocess.run(cmd)
            input(f"\\n{C_GREEN}✅ Processed! Press Enter...{C_RESET}")
        elif c == '3':
            p = get_input_path("Enter Image File Path")
            if not p: continue
            fmt = input("Target format (png/jpg/webp): ").strip().lower()
            if fmt in ['png', 'jpg', 'jpeg', 'webp']:
                im = Image.open(p)
                if fmt in ['jpg', 'jpeg']: im = im.convert('RGB')
                im.save(os.path.splitext(p)[0] + f"_converted.{fmt}")
                input(f"\\n{C_GREEN}✅ Saved! Press Enter...{C_RESET}")
        elif c == '4':
            p = get_input_path("Enter Image File or Folder")
            if not p: continue
            out_pdf = os.path.splitext(p)[0] + "_converted.pdf"
            if os.path.isfile(p):
                Image.open(p).convert('RGB').save(out_pdf)
            else:
                imgs = [os.path.join(p, f) for f in os.listdir(p) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                imgs.sort()
                p_imgs = [Image.open(f).convert('RGB') for f in imgs]
                if p_imgs: p_imgs[0].save(out_pdf, save_all=True, append_images=p_imgs[1:])
            input(f"\\n{C_GREEN}✅ PDF Created! Press Enter...{C_RESET}")
        elif c == '5':
            p = get_input_path("Enter PDF File Path")
            if not p: continue
            out_dir = os.path.splitext(p)[0] + "_images"
            os.makedirs(out_dir, exist_ok=True)
            subprocess.run(["pdftoppm", "-png", p, os.path.join(out_dir, "page")])
            input(f"\\n{C_GREEN}✅ Images Extracted to {out_dir}! Press Enter...{C_RESET}")

if __name__ == "__main__": main()
'''

# 4. Zip Master (A-Z Sorted)
zip_master_code = get_header("ARCHIVE & ZIP MASTER ENGINE") + '''
import zipfile, itertools, string

def get_input_path(prompt_text):
    path = input(f"{C_GREEN}➤ {prompt_text} ([#] Back / [*] Exit): {C_RESET}").strip().strip("\'\\"")
    if path.lower() in ['#', 'b', 'back']: return None
    elif path.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
    if not os.path.exists(path):
        print(f"\\n{C_RED}❌ Error: Path not found!{C_RESET}")
        input("Press Enter...")
        return False
    return path

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Create ZIP File (Compress Folder / Files)")
        print(f"  {C_CYAN}[2]{C_RESET} Extract Normal ZIP Archive (Standard Unzip)")
        print(f"  {C_CYAN}[3]{C_RESET} Unlock / Recover Password-Protected ZIP")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        c = input(f"{C_GREEN}➤ Select Option (1-3): {C_RESET}").strip().lower()
        if c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)
        elif c == '1':
            target = get_input_path("Enter Folder/File to ZIP")
            if target:
                out_zip = target.rstrip("/\\\\") + ".zip"
                with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as z:
                    if os.path.isdir(target):
                        for root, _, files in os.walk(target):
                            for f in files:
                                fp = os.path.join(root, f)
                                z.write(fp, os.path.relpath(fp, os.path.dirname(target)))
                    else: z.write(target, os.path.basename(target))
                input(f"\\n{C_GREEN}✅ Created: {out_zip}! Press Enter...{C_RESET}")
        elif c == '2':
            zp = get_input_path("Enter .zip File Path")
            if zp:
                od = os.path.splitext(zp)[0] + "_extracted"
                os.makedirs(od, exist_ok=True)
                pwd = input("Password (leave blank if none): ").strip()
                try:
                    with zipfile.ZipFile(zp, 'r') as z: z.extractall(od, pwd=pwd.encode() if pwd else None)
                    input(f"\\n{C_GREEN}✅ Extracted to {od}! Press Enter...{C_RESET}")
                except Exception as e: input(f"\\n{C_RED}❌ Error: {e}. Press Enter...{C_RESET}")
        elif c == '3':
            zp = get_input_path("Enter Protected .zip File Path")
            if zp:
                od = os.path.splitext(zp)[0] + "_unlocked"
                os.makedirs(od, exist_ok=True)
                max_l = input("Max length to brute-force (e.g. 4): ").strip()
                max_l = int(max_l) if max_l.isdigit() else 4
                zf = zipfile.ZipFile(zp)
                found = None
                for l in range(1, max_l + 1):
                    if found: break
                    for att in itertools.product(string.digits + string.ascii_lowercase, repeat=l):
                        w = ''.join(att)
                        try:
                            zf.extractall(od, pwd=w.encode())
                            found = w
                            break
                        except Exception: continue
                if found: input(f"\\n{C_GREEN}🎉 Unlocked! Password: {found}. Press Enter...{C_RESET}")
                else: input(f"\\n{C_RED}❌ Password recovery failed. Press Enter...{C_RESET}")

if __name__ == "__main__": main()
'''

files = {
    "menu.py": menu_code,
    "media_dl.py": media_dl_code,
    "converter.py": converter_code,
    "zip_master.py": zip_master_code
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ Professional A-Z sorting applied across Main Dashboard & Submenus!")