import os, sys

print("[*] Generating and populating modular tool suite...")
BASE_DIR = os.path.expanduser("~/modules")

tools_data = {
    "media": [
        ("youtube_downloader.py", 'import os\nprint("--- YouTube Downloader ---")\nurl = input("Enter YouTube URL: ") \nos.system(f"yt-dlp {url}")'),
        ("gif_converter.py", 'print("GIF Converter Tool ready.")'),
        ("image_compressor.py", 'print("Image Compressor Tool ready.")')
    ],
    "network": [
        ("port_scanner.py", 'import socket\nhost=input("Target Host: "); \n[print(f"Port {p}: Open") for p in [21,22,80,443] if socket.socket().connect_ex((host,p))==0]'),
        ("public_ip.py", 'import urllib.request, json\nprint(json.loads(urllib.request.urlopen("https://ipapi.co/json/").read()))')
    ],
    "security": [
        ("aes_vault.py", 'print("AES Vault ready.")'),
        ("jwt_decoder.py", 'print("JWT Decoder ready.")')
    ],
    "recon": [
        ("username_scanner.py", 'print("Username scanner ready.")'),
        ("ip_intel.py", 'import os\nip=input("IP: "); os.system(f"curl ipapi.co/{ip}/json/")'),
        ("exif_extractor.py", 'print("EXIF metadata extractor ready.")')
    ],
    "system": [
        ("storage_cleaner.py", 'import os\nos.system("rm -rf ~/.cache/* 2>/dev/null"); print("Cache cleaned!")'),
        ("battery_inspector.py", 'print("Battery inspector ready.")')
    ],
    "utils": [
        ("temp_mail.py", 'print("Temporary Mail generator ready.")'),
        ("qr_generator.py", 'import urllib.parse\nt=input("Text: "); print("URL:", "https://qrenco.de/"+urllib.parse.quote(t))')
    ]
}

for cat, files in tools_data.items():
    cat_dir = os.path.join(BASE_DIR, cat)
    os.makedirs(cat_dir, exist_ok=True)
    for fname, code in files:
        fpath = os.path.join(cat_dir, fname)
        if not os.path.exists(fpath):
            with open(fpath, "w") as f:
                f.write(code)

print("✅ Modular tool suite populated successfully!")
