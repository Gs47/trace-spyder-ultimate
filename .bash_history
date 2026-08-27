                    progress_callback=engine.callback
                )
                print(f"\n{C_GREEN}✔ Finished:{C_RESET} {dest_path}")
                log_transfer_history("IMPORT", fname, sz_mb, "SUCCESS")
            except Exception as e:
                print(f"\n{C_RED}✖ Download Failed ({fname}): {e}{C_RESET}")
                log_transfer_history("IMPORT", fname, sz_mb, "FAILED")

        input(f"\n{C_GREEN}All downloads completed. Press Enter to continue...{C_RESET}")

async def handle_export(client):
    while True:
        print_banner("EXPORT: UPLOAD FILES")
        print(f" {C_CYAN}[01]{C_RESET} 📤 Upload File to Saved Messages (me)")
        print(f" {C_CYAN}[02]{C_RESET} 📤 Upload File to Channel / Group / User Chat")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Main Hub")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        ch = input(f"\n{C_GREEN}➤ Select Destination (1-2 / 0): {C_RESET}").strip()
        if ch in ['0', 'b', 'back']: break

        chat_target = 'me'
        if ch == '2':
            t = input(f"\n{C_GREEN}➤ Enter Target Channel or Username: {C_RESET}").strip()
            if not t: continue
            chat_target = t

        down_files = sorted(glob.glob(f"{DOWNLOAD_DIR}/*.*"))
        if not down_files:
            print(f"{C_RED}No files found in {DOWNLOAD_DIR}!{C_RESET}")
            input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")
            continue

        print_banner("SELECT FILE FROM DOWNLOADS")
        for idx, fp in enumerate(down_files[:25], 1):
            fn = os.path.basename(fp)
            sz = round(os.path.getsize(fp) / (1024 * 1024), 2)
            print(f"  {C_CYAN}[{idx:02d}]{C_RESET} {C_WHITE}{fn[:40]:<42}{C_RESET} {C_YELLOW}({sz} MB){C_RESET}")

        sel_f = input(f"\n{C_GREEN}➤ Select File Number to Upload: {C_RESET}").strip()
        if not sel_f.isdigit() or not (1 <= int(sel_f) <= len(down_files[:25])):
            continue

        file_to_upload = down_files[int(sel_f) - 1]
        fname = os.path.basename(file_to_upload)
        sz_mb = round(os.path.getsize(file_to_upload) / (1024 * 1024), 2)

        caption = input(f"{C_GREEN}➤ Enter Caption (Optional): {C_RESET}").strip()
        print(f"\n{C_YELLOW}[*] Uploading {fname} ({sz_mb} MB) to {chat_target}...{C_RESET}\n")

        engine = FastProgressEngine(fname, "EXPORT")
        try:
            await client.send_file(
                chat_target,
                file=file_to_upload,
                caption=caption if caption else None,
                progress_callback=engine.callback
            )
            print(f"\n\n{C_GREEN}✅ Success! File uploaded to {chat_target}.{C_RESET}")
            log_transfer_history("EXPORT", fname, sz_mb, "SUCCESS")
        except Exception as e:
            print(f"\n\n{C_RED}✖ Upload Failed: {e}{C_RESET}")
            log_transfer_history("EXPORT", fname, sz_mb, "FAILED")

        input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

async def async_main():
    print_banner("CONNECTING TO TELEGRAM")
    print(f"{C_YELLOW}[*] Initializing High-Speed MTProto Engine...{C_RESET}")

    client = TelegramClient(SESSION_FILE, API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        print_banner("TELEGRAM AUTHENTICATION")
        phone = input(f"{C_GREEN}➤ Enter Phone Number (+91...): {C_RESET}").strip()
        if not phone: return
        
        print(f"\n{C_YELLOW}[*] Sending OTP login code...{C_RESET}")
        await client.send_code_request(phone)
        code = input(f"{C_GREEN}➤ Enter OTP Code: {C_RESET}").strip()
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            pwd = input(f"{C_YELLOW}➤ Two-Step Password: {C_RESET}").strip()
            await client.sign_in(password=pwd)

        print(f"\n{C_GREEN}✔ Authentication Successful!{C_RESET}")
        await asyncio.sleep(1)

    while True:
        print_banner("SELECT OPERATION")
        print(f" {C_CYAN}[01]{C_RESET} 📥 \033[1mIMPORT\033[0m   ➔ Download Media (Fast Single-Line Stream)")
        print(f" {C_CYAN}[02]{C_RESET} 📤 \033[1mEXPORT\033[0m   ➔ Upload Files from Device to Telegram")
        print(f" {C_CYAN}[03]{C_RESET} 📜 \033[1mHISTORY\033[0m  ➔ View Download / Upload Transfer Logs")
        print(f" {C_CYAN}[04]{C_RESET} 🔄 \033[1mLOGOUT\033[0m   ➔ Clear Telegram Session")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Operation (1-4 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': await handle_import(client)
        elif opt == '2': await handle_export(client)
        elif opt == '3': show_history_menu()
        elif opt == '4':
            await client.log_out()
            os.system(f"rm -f {SESSION_FILE}* 2>/dev/null")
            print(f"\n{C_GREEN}✔ Logged out successfully.{C_RESET}")
            await asyncio.sleep(1)
            break

    if client.is_connected():
        await client.disconnect()

def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print(f"\n{C_YELLOW}Session stopped by user.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}❌ Error occurred:{C_RESET}\n")
        traceback.print_exc()
        input(f"\n{C_GREEN}Press Enter to exit...{C_RESET}")

if __name__ == "__main__":
    main()
EOF

chmod +x ~/tg_manager.py
python3 ~/tg_manager.py
# =================================================================
# TELEGRAM PRO ENGINE WITH RECENT 20 CHATS & 25 RECENT MESSAGES
# =================================================================
cat << 'EOF' > ~/tg_manager.py
import os, sys, time, asyncio, shutil, glob, json, traceback
from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeFilename, Channel, Chat, User
from telethon.errors import SessionPasswordNeededError

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

SESSION_FILE = os.path.expanduser("~/.tg_session")
CONFIG_FILE = os.path.expanduser("~/.tg_config.json")
HISTORY_FILE = os.path.expanduser("~/.tg_history.json")
DOWNLOAD_DIR = "/sdcard/Download"

API_ID = 32918286
API_HASH = "f888fdba6d829cf210828f8d4b28b783"

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner(sub="IMPORT & EXPORT HUB"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w
    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_WHITE}{'🕷️  TELEGRAM PRO HUB MANAGER  🕷️'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{'⚡ ═ G O W R I   S H A N K A R ═ ⚡'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{f'🚀 ═ {sub} ═ 🚀'.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def log_transfer_history(op_type, fname, size_mb, status="SUCCESS"):
    records = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                records = json.load(f)
        except: records = []
    
    entry = {
        "type": op_type,
        "filename": fname,
        "size": f"{size_mb:.2f} MB",
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": status
    }
    records.insert(0, entry)
    records = records[:50]
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(records, f, indent=2)
    except: pass

def show_history_menu():
    print_banner("TRANSFER HISTORY & LOGS")
    w = get_screen_width()
    div = "─" * (w - 2)

    if not os.path.exists(HISTORY_FILE):
        print(f"\n{C_RED}No transfer records found yet.{C_RESET}")
    else:
        try:
            with open(HISTORY_FILE, "r") as f:
                records = json.load(f)
            if not records:
                print(f"\n{C_RED}Transfer history is empty.{C_RESET}")
            else:
                print(f"{C_WHITE}{'TYPE':<6} {'DATE / TIME':<19} {'SIZE':<10} {'FILENAME':<22}{C_RESET}")
                print(f"{C_CYAN}{div}{C_RESET}")
                for r in records[:15]:
                    t_lbl = f"{C_GREEN}DL{C_RESET}" if r.get('type') == "IMPORT" else f"{C_MAGENTA}UP{C_RESET}"
                    fn = r.get('filename', 'Unknown')[:20]
                    sz = r.get('size', '0 MB')
                    dt = r.get('date', '')
                    print(f" {t_lbl:<14} {dt:<19} {sz:<10} {C_WHITE}{fn}{C_RESET}")
        except Exception as e:
            print(f"{C_RED}Error reading history: {e}{C_RESET}")

    print(f"\n{C_CYAN}[1]{C_RESET} Clear Transfer History")
    print(f"{C_CYAN}[0]{C_RESET} Back to Main Menu")
    opt = input(f"\n{C_GREEN}➤ Select Option: {C_RESET}").strip()
    if opt == '1':
        if os.path.exists(HISTORY_FILE): os.remove(HISTORY_FILE)
        print(f"{C_GREEN}✔ History cleared successfully!{C_RESET}")
        time.sleep(1)

def get_file_name(msg):
    if msg.file and msg.file.name:
        return msg.file.name
    if msg.media and hasattr(msg.media, 'document') and msg.media.document:
        for attr in msg.media.document.attributes:
            if isinstance(attr, DocumentAttributeFilename):
                return attr.file_name
    return f"Telegram_Media_{msg.id}"

class FastProgressEngine:
    def __init__(self, filename, op_label="DL"):
        self.filename = filename
        self.op_label = op_label
        self.start_time = time.time()
        self.last_update = 0
        self.anim_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.frame_idx = 0

    def callback(self, current, total):
        now = time.time()
        if now - self.last_update < 0.2 and current < total:
            return
        self.last_update = now

        elapsed = max(0.001, now - self.start_time)
        speed = current / elapsed
        if speed >= 1024 * 1024:
            speed_str = f"{speed / (1024 * 1024):.2f}MB/s"
        else:
            speed_str = f"{speed / 1024:.1f}KB/s"

        percent = (current / total) * 100 if total else 0
        eta = (total - current) / speed if speed > 0 and total else 0
        eta_str = f"{int(eta // 60):02d}:{int(eta % 60):02d}"

        bar_len = 10
        filled = int(bar_len * (current / total)) if total else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        spinner = self.anim_frames[self.frame_idx % len(self.anim_frames)]
        self.frame_idx += 1

        mb_cur = current / (1024 * 1024)
        mb_tot = total / (1024 * 1024) if total else 0

        fn_short = self.filename[:14]
        line = (f"\r\033[K{C_YELLOW}{spinner}{C_RESET} {C_CYAN}[{self.op_label}]{C_RESET} "
                f"{C_WHITE}{fn_short:<14}{C_RESET} |{C_GREEN}{bar}{C_RESET}| {percent:5.1f}% "
                f"({mb_cur:.1f}/{mb_tot:.1f}MB) ⚡{C_MAGENTA}{speed_str:<8}{C_RESET} ⏱️{C_YELLOW}{eta_str}{C_RESET}")
        sys.stdout.write(line)
        sys.stdout.flush()

async def select_recent_chat(client, mode_title="SELECT CHAT"):
    print_banner(mode_title)
    print(f"{C_YELLOW}[*] Fetching recent 20 chats / channels / groups...{C_RESET}\n")
    
    dialogs = []
    try:
        async for dialog in client.iter_dialogs(limit=20):
            dialogs.append(dialog)
    except Exception as e:
        print(f"{C_RED}❌ Error fetching chats: {e}{C_RESET}")
        await asyncio.sleep(1)
        return None, None

    if not dialogs:
        print(f"{C_RED}No chats found.{C_RESET}")
        return None, None

    print_banner(f"{mode_title}: RECENT 20 CHATS")
    for idx, d in enumerate(dialogs, 1):
        name = d.name if d.name else "Saved Messages (You)"
        chat_type = "👤 User"
        if d.is_channel: chat_type = "📢 Channel"
        elif d.is_group: chat_type = "👥 Group"
        elif d.entity and getattr(d.entity, 'is_self', False): chat_type = "⭐ Saved"

        print(f"  {C_CYAN}[{idx:02d}]{C_RESET} {C_WHITE}{name[:32]:<34}{C_RESET} {C_YELLOW}({chat_type}){C_RESET}")

    print(f"\n{C_CYAN}[C]{C_RESET} Enter Custom Channel/Group Username or Link manually")
    print(f"{C_CYAN}[0]{C_RESET} Back to Main Hub")

    raw = input(f"\n{C_GREEN}➤ Select Chat Number (1-{len(dialogs)} / C / 0): {C_RESET}").strip()
    if raw in ['0', 'b', 'back']:
        return None, None
    
    if raw.lower() in ['c', 'custom']:
        custom_target = input(f"{C_GREEN}➤ Enter Channel/Group Username, Link or ID: {C_RESET}").strip()
        if custom_target:
            return custom_target, custom_target
        return None, None

    if raw.isdigit() and 1 <= int(raw) <= len(dialogs):
        chosen = dialogs[int(raw) - 1]
        c_name = chosen.name if chosen.name else "Saved Messages"
        return chosen.entity, c_name

    return None, None

async def handle_import(client):
    while True:
        chat_entity, chat_title = await select_recent_chat(client, "IMPORT: CHOOSE SOURCE")
        if not chat_entity: break

        print_banner(f"IMPORT FROM: {str(chat_title)[:22]}")
        print(f"{C_YELLOW}[*] Scanning recent 25 messages for media...{C_RESET}\n")

        messages = []
        try:
            async for msg in client.iter_messages(chat_entity, limit=25):
                if msg.media:
                    messages.append(msg)
        except Exception as e:
            print(f"{C_RED}❌ Error reading messages: {e}{C_RESET}")
            input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")
            continue

        if not messages:
            print(f"{C_RED}❌ No media files found in the last 25 messages of this chat.{C_RESET}")
            input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")
            continue

        print_banner(f"MEDIA FILES ({len(messages)} Found in {str(chat_title)[:18]})")
        for idx, msg in enumerate(messages, 1):
            fn = get_file_name(msg)
            sz = round((msg.file.size or 0) / (1024 * 1024), 2) if msg.file else 0
            date_str = msg.date.strftime("%d/%m %H:%M") if msg.date else ""
            print(f"  {C_CYAN}[{idx:02d}]{C_RESET} {C_WHITE}{fn[:36]:<38}{C_RESET} {C_YELLOW}{sz:>6.1f}MB{C_RESET} {C_MAGENTA}{date_str}{C_RESET}")

        print(f"\n{C_MAGENTA}Tip: Enter space-separated IDs (e.g. 1 3 5) or 'all' to download everything{C_RESET}")
        raw_sel = input(f"\n{C_GREEN}➤ Select File ID(s) to Import: {C_RESET}").strip()
        if raw_sel in ['0', 'b', 'back']: continue

        queue = []
        if raw_sel.lower() == 'all':
            queue = messages[:]
        else:
            for piece in raw_sel.split():
                if piece.isdigit() and 1 <= int(piece) <= len(messages):
                    queue.append(messages[int(piece) - 1])

        if not queue: continue

        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        print(f"\n{C_YELLOW}[+] Starting Download Queue ({len(queue)} files)...{C_RESET}\n")

        for item in queue:
            fname = get_file_name(item)
            dest_path = os.path.join(DOWNLOAD_DIR, fname)
            sz_mb = round((item.file.size or 0) / (1024 * 1024), 2) if item.file else 0
            engine = FastProgressEngine(fname, "IMPORT")
            try:
                await client.download_media(
                    item,
                    file=dest_path,
                    progress_callback=engine.callback
                )
                print(f"\n{C_GREEN}✔ Finished:{C_RESET} {dest_path}")
                log_transfer_history("IMPORT", fname, sz_mb, "SUCCESS")
            except Exception as e:
                print(f"\n{C_RED}✖ Download Failed ({fname}): {e}{C_RESET}")
                log_transfer_history("IMPORT", fname, sz_mb, "FAILED")

        input(f"\n{C_GREEN}All downloads completed. Press Enter to continue...{C_RESET}")

async def handle_export(client):
    while True:
        chat_entity, chat_title = await select_recent_chat(client, "EXPORT: CHOOSE DESTINATION")
        if not chat_entity: break

        down_files = sorted(glob.glob(f"{DOWNLOAD_DIR}/*.*"))
        if not down_files:
            print(f"\n{C_RED}No files found in {DOWNLOAD_DIR}!{C_RESET}")
            input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")
            continue

        print_banner(f"SELECT FILE TO SEND TO: {str(chat_title)[:22]}")
        for idx, fp in enumerate(down_files[:25], 1):
            fn = os.path.basename(fp)
            sz = round(os.path.getsize(fp) / (1024 * 1024), 2)
            print(f"  {C_CYAN}[{idx:02d}]{C_RESET} {C_WHITE}{fn[:40]:<42}{C_RESET} {C_YELLOW}({sz} MB){C_RESET}")

        sel_f = input(f"\n{C_GREEN}➤ Select File Number to Upload (1-{len(down_files[:25])} / 0): {C_RESET}").strip()
        if not sel_f.isdigit() or not (1 <= int(sel_f) <= len(down_files[:25])):
            continue

        file_to_upload = down_files[int(sel_f) - 1]
        fname = os.path.basename(file_to_upload)
        sz_mb = round(os.path.getsize(file_to_upload) / (1024 * 1024), 2)

        caption = input(f"{C_GREEN}➤ Enter Caption (Optional): {C_RESET}").strip()
        print(f"\n{C_YELLOW}[*] Uploading {fname} ({sz_mb} MB) to {chat_title}...{C_RESET}\n")

        engine = FastProgressEngine(fname, "EXPORT")
        try:
            await client.send_file(
                chat_entity,
                file=file_to_upload,
                caption=caption if caption else None,
                progress_callback=engine.callback
            )
            print(f"\n\n{C_GREEN}✅ Success! File sent to {chat_title}.{C_RESET}")
            log_transfer_history("EXPORT", fname, sz_mb, "SUCCESS")
        except Exception as e:
            print(f"\n\n{C_RED}✖ Upload Failed: {e}{C_RESET}")
            log_transfer_history("EXPORT", fname, sz_mb, "FAILED")

        input(f"\n{C_GREEN}Press Enter to continue...{C_RESET}")

async def async_main():
    print_banner("CONNECTING TO TELEGRAM")
    print(f"{C_YELLOW}[*] Initializing High-Speed MTProto Engine...{C_RESET}")

    client = TelegramClient(SESSION_FILE, API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        print_banner("TELEGRAM AUTHENTICATION")
        phone = input(f"{C_GREEN}➤ Enter Phone Number (+91...): {C_RESET}").strip()
        if not phone: return
        
        print(f"\n{C_YELLOW}[*] Sending OTP login code...{C_RESET}")
        await client.send_code_request(phone)
        code = input(f"{C_GREEN}➤ Enter OTP Code: {C_RESET}").strip()
        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            pwd = input(f"{C_YELLOW}➤ Two-Step Password: {C_RESET}").strip()
            await client.sign_in(password=pwd)

        print(f"\n{C_GREEN}✔ Authentication Successful!{C_RESET}")
        await asyncio.sleep(1)

    while True:
        print_banner("SELECT OPERATION")
        print(f" {C_CYAN}[01]{C_RESET} 📥 \033[1mIMPORT\033[0m   ➔ Pick from Recent 20 Chats & Download 25 Media")
        print(f" {C_CYAN}[02]{C_RESET} 📤 \033[1mEXPORT\033[0m   ➔ Pick from Recent 20 Chats & Upload Local Files")
        print(f" {C_CYAN}[03]{C_RESET} 📜 \033[1mHISTORY\033[0m  ➔ View Download / Upload Transfer Logs")
        print(f" {C_CYAN}[04]{C_RESET} 🔄 \033[1mLOGOUT\033[0m   ➔ Clear Telegram Session")
        print(f" {C_CYAN}[0]{C_RESET}  🔙 Back to Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        opt = input(f"\n{C_GREEN}➤ Select Operation (1-4 / 0): {C_RESET}").strip()
        if opt in ['0', 'b', 'back', 'x', 'm']: break

        if opt == '1': await handle_import(client)
        elif opt == '2': await handle_export(client)
        elif opt == '3': show_history_menu()
        elif opt == '4':
            await client.log_out()
            os.system(f"rm -f {SESSION_FILE}* 2>/dev/null")
            print(f"\n{C_GREEN}✔ Logged out successfully.{C_RESET}")
            await asyncio.sleep(1)
            break

    if client.is_connected():
        await client.disconnect()

def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print(f"\n{C_YELLOW}Session stopped by user.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}❌ Error occurred:{C_RESET}\n")
        traceback.print_exc()
        input(f"\n{C_GREEN}Press Enter to exit...{C_RESET}")

if __name__ == "__main__":
    main()
EOF

chmod +x ~/tg_manager.py
python3 ~/tg_manager.py
