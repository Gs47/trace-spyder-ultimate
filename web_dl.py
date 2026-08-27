import sys, os, re, subprocess
import requests
from bs4 import BeautifulSoup

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


DOWNLOAD_DIR = '/sdcard/Download/'

def get_mediafire_direct_link(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        btn = soup.find('a', {'aria-label': 'Download file'}) or soup.find('a', {'id': 'downloadButton'})
        if btn and btn.get('href'):
            return btn.get('href')
    except Exception:
        pass
    return url

def download_file():
    print("=== Universal Web Downloader (MediaFire/Direct/Web) ===")
    url = input("Enter Download Link: ").strip()
    if not url:
        return

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    # മീഡിയഫയർ ലിങ്ക് ആണെങ്കിൽ ഡയറക്ട് ലിങ്ക് എക്സ്ട്രാക്റ്റ് ചെയ്യുന്നു
    if 'mediafire.com' in url.lower():
        print("\nExtracting MediaFire direct download link...")
        url = get_mediafire_direct_link(url)

    print(f"\nTarget Directory: {DOWNLOAD_DIR}")
    print("Starting Multi-Connection Download (16 Parallel Streams)...\n")

    cmd = [
        "aria2c",
        "-x", "16",
        "-s", "16",
        "-k", "1M",
        "--dir", DOWNLOAD_DIR,
        "--summary-interval=1",
        "--console-log-level=warn",
        url
    ]

    try:
        subprocess.run(cmd)
        print("\nDownload Complete!")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    download_file()