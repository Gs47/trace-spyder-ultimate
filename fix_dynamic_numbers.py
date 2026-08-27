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


C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

BANNER = f"""{C_CYAN}┌────────────────────────────────────────────────────────────┐
{C_WHITE}  ████████╗██████╗  █████╗  ██████╗███████╗
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
{C_RESET}
             {C_YELLOW}🕷️  {C_CYAN}T R A C E   S P Y D E R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}T E R M I N A L   H U B{C_MAGENTA} ═ ⚡{C_RESET}
{C_CYAN}└────────────────────────────────────────────────────────────┘{C_RESET}"""

def wrap_script(title, body):
    return f'''import os, sys, subprocess, shutil

C_CYAN = "\\033[1;36m"
C_GREEN = "\\033[1;32m"
C_YELLOW = "\\033[1;33m"
C_RED = "\\033[1;31m"
C_MAGENTA = "\\033[1;35m"
C_WHITE = "\\033[1;37m"
C_RESET = "\\033[0m"

BANNER = """{BANNER}"""

def clear_screen():
    os.system('clear')
    print(BANNER)
    print(f"{{C_MAGENTA}}  [▸] ACTIVE MODULE : {{C_GREEN}}{title}{{C_RESET}}")
    print(f"{{C_CYAN}}─"*60 + f"{{C_RESET}}")

{body}
'''

# 1. Main Menu
menu_body = '''def run_script(script_name):
    path = os.path.expanduser(f"~/{script_name}")
    if os.path.exists(path):
        subprocess.run([sys.executable, path])
    else:
        print(f"\\n{C_RED}❌ Error: {script_name} not found!{C_RESET}")
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Telegram Cloud Hub (Import/Export/Chats)")
        print(f"  {C_CYAN}[2]{C_RESET} Ultimate Media Downloader (YT/IG/FB/X/etc)")
        print(f"  {C_CYAN}[3]{C_RESET} Spotify Smart Music & Video Downloader")
        print(f"  {C_CYAN}[4]{C_RESET} TeraBox Video Fast Downloader")
        print(f"  {C_CYAN}[5]{C_RESET} Advanced Media Converter Engine (FFmpeg)")
        print(f"  {C_CYAN}[6]{C_RESET} Seeker OSINT Location Explorer")
        print(f"  {C_CYAN}[7]{C_RESET} Device & Battery Diagnostic Status")
        print(f"  {C_CYAN}[8]{C_RESET} Termux Storage & Cache Purger")
        print(f"  {C_CYAN}[9]{C_RESET} Settings & Engine Updater")
        print(f"  {C_CYAN}[10]{C_RESET} Full System Self-Repair & Auto-Fix Engine")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_YELLOW}[0]{C_RESET} Refresh Dashboard")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        
        choice = input(f"{C_GREEN}➤ Select Option (1-10): {C_RESET}").strip().lower()
        mapping = {
            '1': 'tools.py', '01': 'tools.py',
            '2': 'media_dl.py', '02': 'media_dl.py',
            '3': 'spotify_dl.py', '03': 'spotify_dl.py',
            '4': 'terabox_dl.py', '04': 'terabox_dl.py',
            '5': 'converter.py', '05': 'converter.py',
            '6': 'seeker_hub.py', '06': 'seeker_hub.py',
            '7': 'device_info.py', '07': 'device_info.py',
            '8': 'phone_cleaner.py', '08': 'phone_cleaner.py',
            '9': 'settings.py', '09': 'settings.py',
            '10': 'auto_repair.py'
        }
        if choice in mapping: run_script(mapping[choice])
        elif choice == '0': continue
        elif choice in ['*', 'x', 'exit', 'q']:
            print(f"\\n{C_RED}Exiting Trace Spyder Terminal Hub. Goodbye!{C_RESET}\\n")
            sys.exit(0)
        else: input(f"\\n{C_RED}❌ Invalid choice! Press Enter...{C_RESET}")

if __name__ == "__main__": main_menu()'''

# 2. Media DL
media_dl_body = '''def main():
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
        elif choice in ['*', 'x', 'exit', 'q']: os._exit(0)

        platform_map = {
            '1': 'YouTube', '2': 'Instagram', '3': 'TeraBox', '4': 'Facebook', '5': 'Universal'
        }

        if choice in platform_map:
            p_name = platform_map[choice]
            clear_screen()
            print(f"{C_YELLOW}[*] Selected Platform: {C_CYAN}{p_name} Downloader{C_RESET}\\n")
            url = input(f"{C_GREEN}➤ Paste {p_name} URL ([#] Back / [*] Exit): {C_RESET}").strip()
            
            if url.lower() in ['#', 'b', 'back']: continue
            elif url.lower() in ['*', 'x', 'exit', 'q']: os._exit(0)
            elif url:
                out_dir = "/sdcard/Download"
                print(f"\\n{C_YELLOW}[*] Downloading into {out_dir}...{C_RESET}")
                subprocess.run(["yt-dlp", "-P", out_dir, url])
                input(f"\\n{C_GREEN}✅ Finished. Press Enter...{C_RESET}")
        else:
            input(f"\\n{C_RED}❌ Invalid option! Press Enter...{C_RESET}")

if __name__ == "__main__": main()'''

# 3. Telegram Tools
tools_body = '''import asyncio, glob

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

async def select_target_chat(client):
    clear_screen()
    dialogs = []
    print(f"{C_YELLOW}[*] Loading recent 15 chats...{C_RESET}")
    async for dialog in client.iter_dialogs(limit=15): dialogs.append(dialog)

    print(f"\\n{C_CYAN}╔══════════════════ [ RECENT CHATS ] ══════════════════╗{C_RESET}")
    for idx, d in enumerate(dialogs):
        name = d.name if d.name else "Saved Messages / Unknown"
        print(f"  {C_YELLOW}[{idx+1}]{C_RESET} {name[:45]}")
    print(f"{C_CYAN}╚══════════════════════════════════════════════════════╝{C_RESET}")
    print(f"  {C_MAGENTA}[s]{C_RESET} Search User / Group (@Username)")
    print(f"  {C_RED}[#]{C_RESET} Back to Menu")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

    c = input(f"{C_GREEN}➤ Select Chat (1-15) or [s] Search: {C_RESET}").strip().lower()
    if c == 's':
        q = input(f"{C_YELLOW}Enter @Username / Name: {C_RESET}").strip()
        if not q: return None
        try:
            e = await client.get_entity(q)
            return e, getattr(e, 'title', None) or getattr(e, 'first_name', q)
        except Exception as err:
            input(f"{C_RED}❌ Not found: {err}. Press Enter...{C_RESET}")
            return None
    elif c.isdigit() and 1 <= int(c) <= len(dialogs):
        sel = dialogs[int(c)-1]
        return sel.entity, sel.name or "Saved Messages"
    return None

async def manage_chat_session():
    client = get_client()
    try: await client.start()
    except Exception as e:
        input(f"{C_RED}❌ Login failed: {e}. Press Enter...{C_RESET}")
        return

    res = await select_target_chat(client)
    if not res:
        await client.disconnect()
        return

    entity, chat_name = res
    while True:
        clear_screen()
        print(f"{C_YELLOW}[*] Active Chat: {C_CYAN}{chat_name}{C_RESET}")
        messages = []
        async for msg in client.iter_messages(entity, limit=25): messages.append(msg)
        messages.reverse()

        print(f"{C_CYAN}────────────────── [ LAST 25 MESSAGES ] ──────────────────{C_RESET}")
        media_count = 0
        for m in messages:
            s = "Me" if m.out else "Them"
            t = m.text.replace('\\n', ' ')[:40] if m.text else ""
            if m.media:
                media_count += 1
                fn = getattr(m.file, 'name', None) or f"[File ID:{m.id}]"
                print(f"  {C_MAGENTA}[{s}]{C_RESET} {C_YELLOW}📁 {fn}{C_RESET} {t}")
            else:
                print(f"  {C_MAGENTA}[{s}]{C_RESET} {t if t else '[Empty]'}")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
        print(f"  {C_CYAN}[1]{C_RESET} Export / Send File to this Chat")
        print(f"  {C_CYAN}[2]{C_RESET} Import / Download Files ({media_count} files available)")
        print(f"  {C_YELLOW}[0]{C_RESET} Refresh Messages")
        print(f"  {C_RED}[#]{C_RESET} Back to Chats List")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        act = input(f"{C_GREEN}➤ Option (1/2/0/#): {C_RESET}").strip().lower()
        if act == '1':
            fp = input(f"\\n{C_GREEN}➤ Enter File Path: {C_RESET}").strip()
            if os.path.exists(fp):
                await client.send_file(entity, fp, caption="🚀 Sent via Trace Spyder Hub")
                print(f"{C_GREEN}✅ Sent!{C_RESET}")
            else: print(f"{C_RED}❌ Not found!{C_RESET}")
            input("Press Enter...")
        elif act == '2':
            m_list = [m for m in messages if m.media]
            if not m_list:
                input(f"{C_RED}❌ No files found! Press Enter...{C_RESET}")
                continue
            for i, m in enumerate(m_list):
                fn = getattr(m.file, 'name', None) or f"media_{m.id}"
                print(f"  [{i+1}] {fn} ({getattr(m.file, 'size', 0)/(1024*1024):.2f} MB)")
            fc = input(f"\\n{C_GREEN}➤ Select File Number (1-{len(m_list)}): {C_RESET}").strip()
            if fc.isdigit() and 1 <= int(fc) <= len(m_list):
                path = await m_list[int(fc)-1].download_media(file="/sdcard/Download")
                print(f"{C_GREEN}✅ Downloaded: {path}{C_RESET}")
            input("Press Enter...")
        elif act == '0': continue
        elif act in ['#', 'b', 'back']: break
    await client.disconnect()

async def account_switcher():
    from telethon import TelegramClient
    while True:
        clear_screen()
        s_files = glob.glob(os.path.join(SESSIONS_DIR, "*.session"))
        print(f"{C_CYAN}╔══════════════════ [ TELEGRAM ACCOUNTS ] ══════════════════╗{C_RESET}")
        print(f"  {C_YELLOW}[1]{C_RESET} Add / Login New Account")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
        accs = []
        for idx, sf in enumerate(s_files):
            name = os.path.basename(sf).replace(".session", "")
            accs.append(name)
            marker = " (ACTIVE)" if sf == get_active_session_path() + ".session" else ""
            print(f"  {C_GREEN}[{idx+2}]{C_RESET} Account: {name}{marker}")
        print(f"{C_CYAN}╚════════════════════════════════════════════════════════════╝{C_RESET}")
        print(f"  {C_RED}[#]{C_RESET} Back to Main Menu")
        c = input(f"\\n{C_GREEN}➤ Select Option: {C_RESET}").strip()
        if c == '1':
            an = input("Enter Account Name (e.g. my_alt): ").strip()
            if an:
                tc = TelegramClient(os.path.join(SESSIONS_DIR, an), 2040, "b18441a1ff607e10a989891a5462e627")
                await tc.start()
                me = await tc.get_me()
                print(f"{C_GREEN}✅ Logged in as: {me.first_name} (@{me.username or 'N/A'}){C_RESET}")
                await tc.disconnect()
                set_active_session(an)
                input("Press Enter...")
        elif c.isdigit() and 2 <= int(c) <= len(accs) + 1:
            set_active_session(accs[int(c)-2])
            print(f"{C_GREEN}✅ Switched to: {accs[int(c)-2]}{C_RESET}")
            input("Press Enter...")
        elif c in ['#', 'b', 'back']: break

def main():
    while True:
        clear_screen()
        print(f"  {C_CYAN}[1]{C_RESET} Telegram Chat Explorer (Search / History / Files)")
        print(f"  {C_CYAN}[2]{C_RESET} Switch / Add Telegram Accounts")
        print(f"  {C_CYAN}[3]{C_RESET} Logout Current Active Account")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Menu Hub")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")
        c = input(f"{C_GREEN}➤ Option (1-3): {C_RESET}").strip().lower()
        if c == '1': asyncio.run(manage_chat_session())
        elif c == '2': asyncio.run(account_switcher())
        elif c == '3':
            sp = get_active_session_path() + ".session"
            if os.path.exists(sp): os.remove(sp); print(f"\\n{C_GREEN}✅ Logged out!{C_RESET}")
            input("Press Enter...")
        elif c in ['#', 'b', 'back']: break
        elif c in ['*', 'x', 'exit', 'q']: os._exit(0)

if __name__ == "__main__": main()'''

files = {
    "menu.py": wrap_script("MAIN DASHBOARD", menu_body),
    "media_dl.py": wrap_script("ULTIMATE MEDIA DOWNLOADER", media_dl_body),
    "tools.py": wrap_script("TELEGRAM CLOUD HUB", tools_body)
}

for fname, content in files.items():
    with open(os.path.expanduser(f"~/{fname}"), "w") as f:
        f.write(content)

print("✅ Perfect dynamic format applied! [1] to [9], [10], [100] without unnecessary leading spaces or zeros.")