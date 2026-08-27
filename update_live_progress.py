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
    return f'''import os, sys, subprocess, shutil, glob, time

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

# 1. Media Downloader with Pro Speed & Stats Bar
media_dl_code = get_header("UNIVERSAL MEDIA DOWNLOADER") + '''
def run_yt_dlp(url, out_dir):
    print(f"\\n{C_YELLOW}[*] Initializing High-Speed Stream Engine...{C_RESET}")
    cmd = [
        "yt-dlp",
        "--progress",
        "--newline",
        "--progress-template",
        "download:[\033[1;32m%(progress._percent_str)s\033[0m] Size: \033[1;36m%(progress._total_bytes_str,progress._total_bytes_estimate_str)s\033[0m | Speed: \033[1;33m%(progress._speed_str)s\033[0m | ETA: \033[1;35m%(progress._eta_str)s\033[0m",
        "-P", out_dir,
        url
    ]
    subprocess.run(cmd)

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
            print(f"{C_YELLOW}[*] Selected Platform: {C_CYAN}{p_name} Pro Downloader{C_RESET}\\n")
            url = input(f"{C_GREEN}➤ Paste {p_name} URL ([#] Back / [*] Exit): {C_RESET}").strip()
            if url.lower() in ['#', 'b', 'back']: continue
            elif url.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
            elif url:
                out_dir = get_download_dir()
                os.makedirs(out_dir, exist_ok=True)
                run_yt_dlp(url, out_dir)
                input(f"\\n{C_GREEN}✅ Download Finished. Press Enter...{C_RESET}")
        else:
            input(f"\\n{C_RED}❌ Invalid option! Press Enter...{C_RESET}")

if __name__ == "__main__": main()
'''

# 2. TeraBox Downloader with Pro Speed
terabox_code = get_header("TERABOX FAST DOWNLOADER") + '''
def main():
    while True:
        clear_screen()
        url = input(f"{C_GREEN}➤ Enter TeraBox Link ([#] Back / [*] Exit): {C_RESET}").strip()
        if url.lower() in ['#', 'b', 'back']: break
        elif url.lower() in ['*', 'x', 'exit', 'q']: sys.exit(0)
        elif url:
            out_dir = get_download_dir()
            os.makedirs(out_dir, exist_ok=True)
            print(f"\\n{C_YELLOW}[*] Connecting to TeraBox High-Speed Server...{C_RESET}")
            cmd = [
                "yt-dlp",
                "--progress",
                "--newline",
                "--progress-template",
                "download:[\033[1;32m%(progress._percent_str)s\033[0m] Size: \033[1;36m%(progress._total_bytes_str,progress._total_bytes_estimate_str)s\033[0m | Speed: \033[1;33m%(progress._speed_str)s\033[0m | ETA: \033[1;35m%(progress._eta_str)s\033[0m",
                "-P", out_dir,
                url
            ]
            subprocess.run(cmd)
            input(f"\\n{C_GREEN}✅ TeraBox Download Finished! Press Enter...{C_RESET}")

if __name__ == "__main__": main()
'''

# 3. Telegram Tools with Visual Progress Bar & Speed Callback
tools_code = get_header("TELEGRAM CLOUD HUB") + '''
import asyncio

SESSIONS_DIR = os.path.expanduser("~/.tg_sessions")
os.makedirs(SESSIONS_DIR, exist_ok=True)
ACTIVE_SESSION_FILE = os.path.expanduser("~/.tg_active_session_name.txt")

def get_active_session_path():
    if os.path.exists(ACTIVE_SESSION_FILE):
        with open(ACTIVE_SESSION_FILE, "r") as f:
            name = f.read().strip()
            if name: return os.path.join(SESSIONS_DIR, name)
    return os.path.join(SESSIONS_DIR, "default_account")

def set_active_session(name):
    with open(ACTIVE_SESSION_FILE, "w") as f: f.write(name)

def get_client():
    from telethon import TelegramClient
    return TelegramClient(get_active_session_path(), 2040, "b18441a1ff607e10a989891a5462e627")

start_time = None
def progress_callback(current, total):
    global start_time
    if not start_time: start_time = time.time()
    elapsed = max(0.001, time.time() - start_time)
    speed = current / elapsed / (1024 * 1024)
    percent = (current / total) * 100
    bar = "█" * int(percent // 4) + "░" * (25 - int(percent // 4))
    sys.stdout.write(f"\\r  [{C_GREEN}{bar}{C_RESET}] {percent:.1f}% | {current/(1024*1024):.2f}/{total/(1024*1024):.2f} MB | Speed: {C_YELLOW}{speed:.2f} MB/s{C_RESET}")
    sys.stdout.flush()

async def manage_chat_session():
    global start_time
    client = get_client()
    try: await client.start()
    except Exception as e:
        input(f"{C_RED}❌ Login failed: {e}. Press Enter...{C_RESET}")
        return

    dialogs = []
    print(f"{C_YELLOW}[*] Loading chats...{C_RESET}")
    async for dialog in client.iter_dialogs(limit=15): dialogs.append(dialog)

    clear_screen()
    print(f"{C_CYAN}╔══════════════════ [ RECENT CHATS ] ══════════════════╗{C_RESET}")
    for idx, d in enumerate(dialogs):
        name = d.name if d.name else "Saved Messages"
        print(f"  {C_YELLOW}[{idx+1}]{C_RESET} {name[:45]}")
    print(f"{C_CYAN}╚══════════════════════════════════════════════════════╝{C_RESET}")
    c = input(f"{C_GREEN}➤ Select Chat (1-15) or [#] Back: {C_RESET}").strip()
    if not (c.isdigit() and 1 <= int(c) <= len(dialogs)):
        await client.disconnect()
        return

    entity, chat_name = dialogs[int(c)-1].entity, dialogs[int(c)-1].name
    while True:
        clear_screen()
        print(f"{C_YELLOW}[*] Active Chat: {C_CYAN}{chat_name}{C_RESET}")
        messages = []
        async for msg in client.iter_messages(entity, limit=20): messages.append(msg)
        messages.reverse()

        print(f"{C_CYAN}────────────────── [ MESSAGES ] ──────────────────{C_RESET}")
        media_count = 0
        for m in messages:
            s = "Me" if m.out else "Them"
            t = m.text.replace('\\n', ' ')[:35] if m.text else ""
            if m.media:
                media_count += 1
                fn = getattr(m.file, 'name', None) or f"[File ID:{m.id}]"
                print(f"  {C_MAGENTA}[{s}]{C_RESET} {C_YELLOW}📁 {fn}{C_RESET} {t}")
            else:
                print(f"  {C_MAGENTA}[{s}]{C_RESET} {t if t else '[Empty]'}")
        print(f"{C_CYAN}──────────────────────────────────────────────────{C_RESET}")
        print(f"  {C_CYAN}[1]{C_RESET} Send File with Live Upload Speed")
        print(f"  {C_CYAN}[2]{C_RESET} Download File with Live Progress & Speed")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Chats")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        act = input(f"{C_GREEN}➤ Option: {C_RESET}").strip().lower()
        if act == '1':
            fp = input(f"\\n{C_GREEN}➤ File Path: {C_RESET}").strip().strip("\'\\"")
            if os.path.exists(fp):
                start_time = None
                print(f"\\n{C_YELLOW}[*] Uploading to Telegram...{C_RESET}")
                await client.send_file(entity, fp, progress_callback=progress_callback)
                print(f"\\n{C_GREEN}✅ Upload Complete!{C_RESET}")
            else: print(f"{C_RED}❌ Not found!{C_RESET}")
            input("Press Enter...")
        elif act == '2':
            m_list = [m for m in messages if m.media]
            if not m_list:
                input(f"{C_RED}❌ No files! Press Enter...{C_RESET}")
                continue
            for i, m in enumerate(m_list):
                fn = getattr(m.file, 'name', None) or f"file_{m.id}"
                print(f"  [{i+1}] {fn} ({getattr(m.file, 'size', 0)/(1024*1024):.2f} MB)")
            fc = input(f"\\n{C_GREEN}➤ Select File (1-{len(m_list)}): {C_RESET}").strip()
            if fc.isdigit() and 1 <= int(fc) <= len(m_list):
                start_time = None
                out_d = get_download_dir()
                print(f"\\n{C_YELLOW}[*] Downloading from Telegram...{C_RESET}")
                await m_list[int(fc)-1].download_media(file=out_d, progress_callback=progress_callback)
                print(f"\\n{C_GREEN}✅ Download Complete! Saved to {out_d}{C_RESET}")
            input("Press Enter...")
        elif act in ['#', 'b', 'back']: break
    await client.disconnect()

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Telegram Chat Explorer (Files & Live Speeds)")
        print(f"  {C_CYAN}[2]{C_RESET} Logout Current Active Account")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1-2): {C_RESET}").strip().lower()
        if c == '1': asyncio.run(manage_chat_session())
        elif c == '2':
            sp = get_active_session_path() + ".session"
            if os.path.exists(sp): os.remove(sp); print(f"\\n{C_GREEN}✅ Logged out!{C_RESET}")
            input("Press Enter...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: sys.exit(0)

if __name__ == "__main__": main()
'''

files = {
    "media_dl.py": media_dl_code,
    "terabox_dl.py": terabox_code,
    "tools.py": tools_code
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ Live Progress Bar, Speed (MB/s), ETA & Percentage stats enabled across all downloaders!")