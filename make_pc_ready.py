import os, sys

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


def get_cross_platform_header(title):
    return f'''import os, sys, subprocess, shutil, glob

C_CYAN = "\\033[1;36m"
C_GREEN = "\\033[1;32m"
C_YELLOW = "\\033[1;33m"
C_RED = "\\033[1;31m"
C_MAGENTA = "\\033[1;35m"
C_WHITE = "\\033[1;37m"
C_RESET = "\\033[0m"

BANNER = f"""{{C_CYAN}}┌────────────────────────────────────────────────────────────┐
{{C_WHITE}}  ████████╗██████╗  █████╗  ██████╗███████╗
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
{{C_RESET}}
         {{C_YELLOW}}🕷️  {{C_CYAN}}G O W R I   S H A N K A R{{C_YELLOW}}  🕷️{{C_RESET}}
           {{C_MAGENTA}}⚡ ═ {{C_GREEN}}T E R M I N A L   H U B{{C_MAGENTA}} ═ ⚡{{C_RESET}}
{{C_CYAN}}└────────────────────────────────────────────────────────────┘{{C_RESET}}"""

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

# 1. Media Downloader
media_dl_code = get_cross_platform_header("ULTIMATE MEDIA DOWNLOADER") + '''
def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} YouTube Video / Shorts / Playlist")
        print(f"  {C_CYAN}[2]{C_RESET} Instagram Reels / Post / Story")
        print(f"  {C_CYAN}[3]{C_RESET} TeraBox Fast Video Downloader")
        print(f"  {C_CYAN}[4]{C_RESET} Facebook Video Downloader")
        print(f"  {C_CYAN}[5]{C_RESET} X (Twitter) / TikTok / Others (Universal)")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        choice = input(f"{C_GREEN}➤ Select Platform (1-5): {C_RESET}").strip().lower()
        if choice in ['#', 'b', 'back']: break
        elif choice in ['*', 'x', 'exit', 'q']: sys.exit(0)

        platform_map = {'1': 'YouTube', '2': 'Instagram', '3': 'TeraBox', '4': 'Facebook', '5': 'Universal'}
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

# 2. Spotify Downloader
spotify_dl_code = get_cross_platform_header("SPOTIFY MUSIC DOWNLOADER") + '''
def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Spotify Song / Album / Playlist Downloader")
        print(f"  {C_CYAN}[2]{C_RESET} Spotify Video / Canvas Downloader")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        choice = input(f"{C_GREEN}➤ Select Option (1-2): {C_RESET}").strip().lower()
        if choice in ['#', 'b', 'back']: break
        elif choice in ['*', 'x', 'exit', 'q']: sys.exit(0)

        out_music = get_music_dir()
        out_video = get_download_dir()
        os.makedirs(out_music, exist_ok=True)
        os.makedirs(out_video, exist_ok=True)

        if choice == '1':
            while True:
                clear_screen()
                print(f"{C_YELLOW}[*] Spotify Audio Downloader{C_RESET}")
                print(f"{C_CYAN}─"*60 + f"{C_RESET}")
                url = input(f"{C_GREEN}➤ Enter Spotify Link ([#] Back / [*] Exit): {C_RESET}").strip()
                if url.lower() in ['#', 'b', 'back']: break
                elif url.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
                elif not url: continue

                est_tracks = 20 if ("playlist" in url.lower() or "album" in url.lower()) else 1
                print(f"\\n{C_CYAN}╔════════════════════════════════════════════════════════════╗{C_RESET}")
                print(f"  {C_GREEN}📊 QUALITY & ESTIMATED SIZES:{C_RESET}")
                print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
                print(f"  {C_WHITE}[1] 320 kbps (Extreme)     ~{est_tracks * 9} MB (~9MB/track){C_RESET}")
                print(f"  {C_WHITE}[2] 160 kbps (High Quality) ~{est_tracks * 5} MB (~5MB/track){C_RESET}")
                print(f"  {C_WHITE}[3] 96 kbps (Normal Saver)  ~{est_tracks * 3} MB (~3MB/track){C_RESET}")
                print(f"{C_CYAN}╚════════════════════════════════════════════════════════════╝{C_RESET}")
                
                qc = input(f"\\n{C_GREEN}➤ Choose Quality (1/2/3) or [#] Back: {C_RESET}").strip().lower()
                if qc in ['#', 'b', 'back']: continue
                elif qc in ['*', 'x', 'exit', 'q']: sys.exit(0)

                bitrate = "160k" if qc == '2' else ("96k" if qc == '3' else "320k")
                print(f"\\n{C_YELLOW}[*] Downloading tracks into {out_music}...{C_RESET}")
                subprocess.run(["spotdl", url, "--output", out_music, "--audio", bitrate])
                input(f"\\n{C_GREEN}✅ Download Complete! Press Enter...{C_RESET}")
                break
        elif choice == '2':
            while True:
                clear_screen()
                print(f"{C_YELLOW}[*] Spotify Video Downloader{C_RESET}")
                print(f"{C_CYAN}─"*60 + f"{C_RESET}")
                url = input(f"{C_GREEN}➤ Enter Video Link ([#] Back / [*] Exit): {C_RESET}").strip()
                if url.lower() in ['#', 'b', 'back']: break
                elif url.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
                elif url:
                    subprocess.run(["yt-dlp", "-P", out_video, url])
                    input(f"\\n{C_GREEN}✅ Finished. Press Enter...{C_RESET}")
                    break

if __name__ == "__main__": main()
'''

with open(os.path.expanduser("~/media_dl.py"), "w") as f: f.write(media_dl_code)
with open(os.path.expanduser("~/spotify_dl.py"), "w") as f: f.write(spotify_dl_code)

print("✅ Scripts converted to 100% Cross-Platform (Windows & Android ready)!")