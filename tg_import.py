import sys, os, time
from telethon.sync import TelegramClient

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


API_ID = 32918286
API_HASH = 'f888fdba6d829cf210828f8d4b28b783'
DOWNLOAD_DIR = '/sdcard/Download/'

client = TelegramClient('my_session', API_ID, API_HASH)

last_time = time.time()
last_bytes = 0

def progress_callback(current, total):
    global last_time, last_bytes
    current_time = time.time()
    time_diff = current_time - last_time
    
    if time_diff >= 0.8:
        speed = (current - last_bytes) / time_diff
        eta = (total - current) / speed if speed > 0 else 0
        
        cur_mb = current / (1024 * 1024)
        tot_mb = total / (1024 * 1024)
        pct = (current / total) * 100
        spd_mb = speed / (1024 * 1024)
        
        # സ്ക്രീനിൽ ഒതുങ്ങുന്ന ചെറിയ ഒറ്റ വരി ഫോർമാറ്റ്
        status = f"\r[{pct:4.1f}%] {cur_mb:.1f}/{tot_mb:.1f}MB | {spd_mb:.2f}MB/s | ETA:{int(eta)}s"
        sys.stdout.write(status.ljust(50))
        sys.stdout.flush()
        
        last_time = current_time
        last_bytes = current

def main():
    client.start()
    print("--- Telegram Import ---")
    dialogs = client.get_dialogs(limit=20)
    for i, d in enumerate(dialogs, 1): 
        print(f"[{i}] {d.name}")
    
    chat_idx = int(input("\nSelect Chat: ")) - 1
    chat = dialogs[chat_idx]
    
    msgs = [m for m in client.get_messages(chat.entity, limit=20) if m.media]
    for i, m in enumerate(msgs, 1):
        file_size = (m.file.size / (1024*1024)) if m.file else 0
        file_name = m.file.name if m.file and m.file.name else f"File_{i}"
        print(f"[{i}] {file_name} ({file_size:.1f} MB)")
        
    choice = int(input("\nSelect File: ")) - 1
    msg = msgs[choice]
    
    print("\nDownloading...")
    client.download_media(msg, file=DOWNLOAD_DIR, progress_callback=progress_callback)
    print("\nDone!")

with client:
    main()