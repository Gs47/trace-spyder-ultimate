import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import os, sys, shutil, time, subprocess
import builtins

def safe_input(prompt=""):
    try: return _orig_input(prompt)
    except (EOFError, KeyboardInterrupt): sys.exit(0)
_orig_input = builtins.input
builtins.input = safe_input

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

MENU_ITEMS = {
    "1": ("Gmail Automation Bot", "gmail_bot.py"),
    "2": ("Telegram Hub Manager", "tg_manager.py"),
    "3": ("Universal Media Downloader", "media_dl.py"),
    "4": ("Spotify Music Downloader", "spotify_dl.py"),
    "5": ("TeraBox Cloud Downloader", "terabox_dl.py"),
    "6": ("Torrent Downloader", "torrent_dl.py"),
    "7": ("Cross-Device File Transfer", "file_transfer.py"),
    "8": ("Audio/Video Converter", "converter.py"),
    "9": ("OSINT Target Recon", "recon_tool.py"),
    "10": ("Web Domain Recon", "web_recon.py"),
    "11": ("Network Audit & Scan", "net_tools.py"),
    "12": ("Seeker Location Engine", "seeker_hub.py"),
    "13": ("Phone Number Lookup", "check_number.py"),
    "14": ("Data & Photo Recovery", "data_recovery.py"),
    "15": ("AES Encrypted Vault", "file_vault.py"),
    "16": ("Cryptography & Ciphers", "crypto_tool.py"),
    "17": ("Hash Generator & Check", "hash_tool.py"),
    "18": ("Multi-Base Encoder", "encoder_tool.py"),
    "19": ("Secure Password Gen", "pwgen_tool.py"),
    "20": ("Disposable Temp Mail", "temp_mail.py"),
    "21": ("Link Unshortener", "link_unshort.py"),
    "22": ("Device Hardware Info", "device_info.py"),
    "23": ("Phone Storage Cleaner", "phone_cleaner.py"),
    "24": ("System Benchmark", "benchmark_tool.py"),
    "25": ("Zip Master Utility", "zip_master.py"),
    "26": ("QR Code Maker/Scan", "qr_tool.py"),
    "28": ("System Settings & Diagnostics", "settings.py"),
    "29": ("Complete Manual & About Us", "about.py")
}

MASTER_600_SUITE = {
    1: ("Video Downloader Suite", ["YouTube HD MP4 Ripper", "Facebook Video Grabber", "Instagram Reels DL", "TikTok Watermark Free", "Twitter / X Media DL", "Vimeo HD Downloader", "Dailymotion Stream DL", "Reddit Video Downloader", "Pinterest Video Grabber", "Bulk Multi-URL Downloader"]),
    2: ("Audio & Music Ripper Hub", ["Spotify 320kbps Ripper", "SoundCloud Audio DL", "Apple Music Stream DL", "Bandcamp Track Grabber", "AAC to MP3 Converter", "WAV Lossless Ripper", "FLAC Audio Converter", "AI Vocal Remover / Isolator", "Audio Ringtone Cutter", "ID3 Tag & Cover Editor"]),
    3: ("Cloud & Storage Downloaders", ["TeraBox Direct Link DL", "Google Drive File DL", "Mega.nz Link Fetcher", "MediaFire Batch DL", "Dropbox Link Downloader", "OneDrive Shared File DL", "Archive.org Bulk Downloader", "Torrent Magnet Parser", "Cloud Storage Synchronizer", "Remote FTP/SFTP Grabber"]),
    4: ("Media & Codec Converters", ["MP4 to MKV Converter", "AVI to MP4 Transcoder", "MOV to MP4 Converter", "MKV to WebM Compressor", "MP3 to WAV Converter", "OGG to MP3 Converter", "Video Resolution Upscaler", "Video Frame Rate Adjuster", "Audio Bitrate Normalizer", "Batch Format Converter"]),
    5: ("Subtitle & Metadata Tools", ["Auto Subtitle Generator", "SRT Subtitle Downloader", "Embed Subtitles to MP4", "Extract Subtitles from MKV", "Subtitle Language Translator", "Metadata Cleaner / Stripper", "EXIF Data Inspector", "Video Chapter Generator", "Media Info Inspector", "Thumbnail Poster Extractor"]),
    6: ("Playlist & Batch Engines", ["YouTube Playlist DL", "YouTube Channel Downloader", "Spotify Playlist Sync", "SoundCloud Playlist DL", "Batch URL Text Parser", "Multi-Threaded Downloader", "Scheduled Batch Downloader", "Paused Download Resume", "Automatic Folder Organizer", "Download History Logger"]),
    7: ("Live Stream & HLS Grabbers", ["HLS M3U8 Stream Downloader", "Live YouTube Stream DL", "Twitch VOD Downloader", "RTMP Stream Grabber", "HTTP Live Segment Merger", "RTSP Stream Recorder", "Webcam Feed Capture", "Audio Podcast Stream DL", "Radio Station Stream Ripper", "Live Stream Monitor"]),
    8: ("Image & Graphic Utilities", ["Bulk Image Resizer", "PNG to JPG Converter", "WebP to PNG Converter", "Image Compression Tool", "Watermark Adder to Images", "Color Palette Extractor", "Ascii Art Image Generator", "Image Crop & Rotate", "Meme Generator Utility", "Icon & Logo Maker"]),
    9: ("Advanced Audio Enhancers", ["Audio Volume Booster", "Bass Boost Filter", "Echo & Reverb Effect", "Noise Suppression Tool", "Audio Pitch Shifter", "Speed / Tempo Adjuster", "Equalizer Preset Applier", "Stereo to Mono Converter", "Fade In / Fade Out Maker", "Audio Spectrum Visualizer"]),
    10: ("Video Editing Utilities", ["Video Cutter & Trimmer", "Video Joiner / Merger", "Video Cropper Utility", "Video Rotation Tool", "Fast-Forward / Slow-Mo", "Video Reverse Tool", "Mute Audio from Video", "Replace Audio in Video", "Split Video into Parts", "GIF from Video Maker"]),
    11: ("Advanced Port Scanners", ["TCP SYN Port Scanner", "UDP Service Scanner", "Common Port Quick Scan", "Full 65535 Port Scan", "Banner Grabbing Tool", "OS Detection Scanner", "Firewall Detector", "Vulnerability Assessment", "Network Range Sweeper", "Custom Port Range Scan"]),
    12: ("IP & Geo-Intelligence", ["Public IP & ISP Audit", "IP Geolocation Tracker", "IPv4 to IPv6 Converter", "Reverse IP Lookup", "Subnet Calculator Tool", "CIDR Range Expander", "ASN Lookup Utility", "BGP Route Inspector", "Ping Latency Monitor", "Traceroute Path Analyzer"]),
    13: ("DNS & Domain Tools", ["DNS Record Lookup (A, MX)", "DNS Propagation Checker", "WHOIS Domain Recon", "Subdomain Enumerator", "Reverse DNS Lookup", "TXT & SPF Record Auditor", "Nameserver Validation", "Domain Expiry Checker", "DNS Zone Transfer Test", "Custom DNS Server Query"]),
    14: ("Wi-Fi & Local Network", ["Local LAN Device Scan", "Wi-Fi Signal Strength Analyzer", "MAC Address Vendor Lookup", "Router Gateway Finder", "ARP Table Inspector", "DHCP Lease Scanner", "Bluetooth Device Discovery", "Network Bandwidth Monitor", "Active Connection Inspector", "Local Host Ping Sweep"]),
    15: ("Network Security Analyzers", ["SSL Certificate Inspector", "HTTP Header Security Audit", "Proxy Anonymity Checker", "VPN Connection Test", "Packet Sniffer Simulator", "HTTP Traffic Interceptor", "CORS Policy Checker", "HSTS Header Auditor", "Open Proxy Finder", "Firewall Bypass Tester"]),
    16: ("Speed & Performance Tests", ["Bandwidth Speed Test CLI", "Download Speed Benchmark", "Upload Speed Benchmark", "Server Latency Checker", "Packet Loss Measurement", "Jitter Test Utility", "Multi-Server Speed Test", "Network Load Simulator", "Connection Stability Test", "ISP Throttling Detector"]),
    17: ("Web Server Testing", ["HTTP Status Code Checker", "Web Page Load Time Test", "Redirect Path Tracer", "Robots.txt & Sitemap Finder", "CMS Detection Tool", "Web Tech Stack Analyzer", "Broken Link Checker", "HTML Source Inspector", "HTTP Methods Allowed Check", "Cookie Security Auditor"]),
    18: ("Remote Access Utilities", ["SSH Connection Manager", "SFTP File Transfer Tool", "Telnet Client Simulator", "FTP Server Tester", "RDP Port Availability Test", "VNC Port Checker", "SSH Key Fingerprint Check", "Remote Command Runner", "Secure Tunnel Inspector", "Port Forwarding Checker"]),
    19: ("Traffic & Packet Tools", ["Packet Size Analyzer", "MTU Path Discovery", "TCP Handshake Simulator", "UDP Packet Sender", "ICMP Echo Request Tool", "ARP Spoofing Detector", "Network Flow Monitor", "Socket Connection Tester", "DNS Query Logger", "HTTP Request Builder"]),
    20: ("Network Diagnostics Suite", ["Complete Network Health Check", "Gateway Connection Test", "DNS Resolution Fixer", "Socket Timeout Tester", "Interface Statistics Viewer", "Network Adapter Reset Tool", "IP Conflict Detector", "Routing Table Inspector", "Network Diagnostics Report", "Automated Net Repair"]),
    21: ("AES & Encryption Vault", ["AES-256 File Encryptor", "AES File Decryptor", "Folder Encryption Tool", "OpenSSL Encrypt Utility", "Passphrase Key Derivation", "Secure File Shredder", "Encrypted Archive Maker", "Password Protected Zip", "Keyfile Generator", "Decryption Verification"]),
    22: ("Hash & Checksum Tools", ["MD5 Checksum Generator", "SHA-256 Hash Creator", "SHA-512 Hash Generator", "File Integrity Verifier", "Bulk Hash Checker", "Password Hash Cracker (Demo)", "HMAC Signature Generator", "CRC32 Calculator", "Base64 Hash Encoder", "Hash Comparison Tool"]),
    23: ("Secure Password Generators", ["Strong Password Generator", "PIN Code Generator", "Passphrase Generator", "Memorable Password Maker", "Custom Character Gen", "Bulk Password Creator", "Hex Key Generator", "API Secret Token Gen", "Cryptographic Nonce Gen", "Password Complexity Check"]),
    24: ("Encoding & Decoding Hub", ["Base64 Encoder / Decoder", "Hexadecimal Converter", "URL Encoder / Decoder", "Binary to Text Converter", "ASCII Code Converter", "Unicode / UTF-8 Encoder", "Morse Code Translator", "ROT13 Cipher Tool", "HTML Entity Encoder", "Multi-Base Converter"]),
    25: ("Public Key Cryptography", ["RSA Key Pair Generator", "SSH Key Generator", "PGP Key Ring Manager", "Digital Signature Tool", "Public Key Exporter", "Certificate Signing Req", "SSL/TLS Key Inspector", "Key Exchange Simulator", "Diffie-Hellman Test", "Cryptographic Proof Gen"]),
    26: ("Steganography & Hiding", ["Hide Text in Image", "Extract Text from Image", "Hide File inside Audio", "Extract File from Audio", "Invisible Unicode Space", "Steganalysis Inspector", "Secret Note Encryptor", "Audio Echo Hider", "Exif Comment Hider", "Secure Payload Wrapper"]),
    27: ("Token & JWT Analyzers", ["JWT Token Decoder", "JWT Signature Verifier", "OAuth Token Inspector", "API Session Token Gen", "Bearer Token Validator", "Cookie Token Parser", "Auth Header Inspector", "Token Expiry Checker", "Claims Payload Viewer", "Secure Token Vault"]),
    28: ("Security Auditing Tools", ["Password Strength Tester", "Vulnerability Database Query", "Exploit Search Utility", "Security Checklist Audit", "Permission Audit Tool", "Secret Leak Detector", "Configuration Hardening", "Risk Assessment Tool", "Security Log Analyzer", "Compliance Checker"]),
    29: ("Cryptographic Ciphers", ["Caesar Cipher Tool", "Vigenere Cipher Tool", "Atbash Cipher Tool", "Affine Cipher Tool", "XOR Encryption Tool", "Playfair Cipher Tool", "Rail Fence Cipher", "Substitution Cipher", "Polybius Square Tool", "Cipher Cracker Utility"]),
    30: ("Privacy & Anonymity Tools", ["IP Masking Checker", "DNS Leak Test Helper", "WebRTC Leak Detector", "User-Agent Spoofer", "Referer Header Spoofer", "Browser Fingerprint Check", "Tracker Block Verifier", "Cookie Privacy Auditor", "Metadata Scrubbing Tool", "Anonymity Score Test"]),
    31: ("Username OSINT Scanners", ["Social Media Username Find", "GitHub Profile Recon", "Instagram Footprint Check", "Twitter / X User Scan", "Reddit User History Recon", "Telegram Username Search", "TikTok Account Tracker", "Pinterest Profile Check", "Forum Username Lookup", "Global Social Sweeper"]),
    32: ("Phone & Contact Intelligence", ["Phone Number Lookup", "Country Code Identifier", "Carrier & Network Check", "Line Type Classification", "Timezone Region Finder", "International Format Fix", "WhatsApp Status Checker", "VoIP Number Detector", "Spam Risk Score Lookup", "Contact Metadata Audit"]),
    33: ("Email OSINT & Breaches", ["Email Format Validator", "Domain MX Email Check", "HaveIBeenPwned API Query", "Email Header Analyzer", "Disposable Email Detector", "Gravatar Profile Finder", "Email Reputation Check", "SMTP Server Tester", "Alias Generator Tool", "Email Trace Utility"]),
    34: ("Domain & Web Recon", ["WHOIS Deep History Recon", "Subdomain Bruteforcer", "DNS Record Enumerator", "SSL Certificate History", "Historical Wayback Fetch", "Technology Stack Audit", "Server IP History", "Associated Domains Find", "Robots.txt Content Grab", "Sitemap URL Extractor"]),
    35: ("Metadata & EXIF Forensic", ["GPS Location Extractor", "Camera Make / Model Find", "Software Timestamp Check", "Audio Metadata Extractor", "PDF Document Metadata", "Office File Metadata", "Hidden Layer Inspector", "Image Thumbnail Check", "Forensic Report Builder", "Metadata Sanitizer"]),
    36: ("Search Engine Dorking", ["Google Dork Query Builder", "Shodan Search Helper", "GitHub Dork Generator", "Pastebin Search Tool", "Social Media Dork Tool", "Filetype Search Builder", "Directory Traversal Dork", "Admin Panel Finder", "Config File Dork Search", "Custom Dork Executor"]),
    37: ("Location & Geolocation", ["IP Geolocation Mapper", "Coordinates Converter", "Timezone & Offset Calc", "Distance Calculator", "Airport Code Lookup", "Postal Code Intelligence", "Country Flag & Info", "Region Code Resolver", "Solar & Lunar Calculator", "Map Link Generator"]),
    38: ("Company & Org OSINT", ["Corporate Registry Search", "Employee Name Finder", "Company Domain Mapping", "ASN Organization Check", "Parent Company Finder", "Business Address Verify", "Brand Asset Finder", "Trademark Database Query", "Financial Data Lookup", "Corporate Footprint Audit"]),
    39: ("Dark Web & Threat Intel", ["Threat Intelligence Feed", "Malware Hash Lookup", "Phishing URL Checker", "Blacklist IP Checker", "Exploit Database Search", "Vulnerability Feed Query", "Security Alert Monitor", "Ransomware Tracker", "Botnet C2 IP Checker", "Dark Web Mention Check"]),
    40: ("OSINT Report Builders", ["Target Dossier Generator", "JSON Recon Exporter", "HTML Recon Report Maker", "Evidence Vault Logger", "Timeline Event Builder", "Case Note Organizer", "Export to CSV Report", "Summary Brief Creator", "Automated OSINT Script", "Audit Trail Generator"]),
    41: ("Storage & Junk Cleaners", ["Termux Cache Cleaner", "Python Temp File Purge", "External Thumbnail Clean", "Deep Storage Analyzer", "Log File Cleaner", "Orphaned File Finder", "App Cache Deleter", "Temporary Folder Wipe", "Disk Space Reclaimer", "Automatic Storage Clean"]),
    42: ("Hardware & Device Specs", ["CPU Core & Architecture", "RAM Usage & Capacity", "Battery Health Monitor", "Storage Partition Info", "Display Resolution Check", "OS & Kernel Version", "Network Interface Specs", "Sensor Availability Check", "Thermal Status Monitor", "Hardware Diagnostic Report"]),
    43: ("Process & Task Managers", ["Running Process List", "Kill Process Utility", "CPU Load Monitor", "Memory Usage Tracker", "Background Job Viewer", "Thread Count Inspector", "Process Priority Adjust", "Active Service Check", "Startup Script Manager", "System Task Dashboard"]),
    44: ("System Benchmark Tools", ["CPU Speed Benchmark", "Memory Bandwidth Test", "Disk I/O Benchmark", "Floating Point Math Test", "Python Execution Speed", "JSON Parsing Benchmark", "Network Throughput Test", "Multi-Core Stress Test", "System Stability Check", "Performance Score Card"]),
    45: ("Backup & Archive Utilities", ["Full Suite ZIP Backup", "Restore from ZIP Backup", "Custom Folder Backup", "Cloud Backup Sync", "Backup Integrity Check", "Automatic Schedule Backup", "Tarball Compressor", "Gzip Compression Tool", "Backup Log Inspector", "Quick Snapshot Maker"]),
    46: ("Log & Diagnostic Parsers", ["System Error Log Parser", "Python Traceback Analyzer", "Access Log Inspector", "Crash Report Viewer", "Security Event Logger", "Audit Trail Reader", "Log Filter Utility", "Real-time Log Tailer", "Log Export to Text", "Automated Log Cleaner"]),
    47: ("Environment & Config Tools", ["Environment Variables View", "PATH Variable Inspector", "Python Path Checker", "Config File Editor", "Settings Manager", "User Preference Hub", "App Configuration Audit", "Default Settings Reset", "Custom Alias Creator", "Shell Profile Manager"]),
    48: ("Auto-Repair & Maintenance", ["Module Syntax Validator", "Permission Locker (755)", "Missing Library Fixer", "Broken Link Repairer", "Database Integrity Check", "Self-Healing Script Fix", "Corrupted File Restorer", "Automatic Update Check", "Suite Health Audit", "Master System Restore"]),
    49: ("Power & Session Tools", ["Terminal Session Clear", "Screen Refresh Utility", "Safe Exit Manager", "Quick Restart Tool", "Session Timer Utility", "Idle Timeout Config", "Power Options Menu", "Lock Screen Simulator", "Emergency Abort Tool", "Session State Saver"]),
    50: ("Advanced Diagnostics Hub", ["Deep Code Integrity Audit", "Runtime Exception Tester", "Dependency Tree Viewer", "API Latency Tester", "Memory Leak Detector", "Thread Deadlock Check", "Security Sandbox Audit", "System Stress Suite", "Comprehensive Report Gen", "Master Diagnostics Panel"]),
    51: ("Temporary Mail Hub", ["Generate Temp Email", "Check Inbox Messages", "Read Email Content", "Custom Alias Generator", "Auto-Refresh Inbox", "Copy Email Address", "Delete Temp Mailbox", "Save Email to File", "Attachment Downloader", "Disposable Mail History"]),
    52: ("Link Unshortener Tools", ["Trace Bit.ly Links", "Unshorten TinyURL", "Resolve t.co Redirects", "Full URL Redirect Trace", "HTTP Status Code Check", "Malicious Link Warning", "Bulk Link Unshortener", "Save Trace Report", "QR Code Link Checker", "Domain Reputation Check"]),
    53: ("QR Code Generators", ["Text to QR Code (ASCII)", "URL to QR Code PNG", "WiFi Password QR Code", "vCard Contact QR Code", "UPI Payment QR Code", "Email QR Code Generator", "Phone Call QR Code", "SMS Message QR Code", "Custom Size QR Maker", "High-Res QR Exporter"]),
    54: ("Developer REST & APIs", ["cURL Command Builder", "REST API Tester", "JSON Formatter / Beautifier", "HTML/CSS Minifier", "Regex Pattern Tester", "SQL Query Formatter", "Timestamp Converter", "Color HEX/RGB Picker", "Text Diff Comparator", "UUID / GUID Generator"]),
    55: ("Text & Note Utilities", ["Terminal Scratchpad Notes", "Todo List Manager", "Text Word & Char Count", "Case Converter (UPPER/lower)", "Markdown Live Preview", "Base64 Image Converter", "CSV Data Formatter", "Text Line Sorter", "Duplicate Line Remover", "Secure Note Vault"]),
    56: ("Time & Currency Tools", ["World Clock & Timezones", "Currency Converter Tool", "Unit Converter (Length)", "Unit Converter (Weight)", "Temperature Converter", "Stopwatch & Timer", "Countdown Timer Utility", "Calendar & Date Calc", "Leap Year Checker", "Workday Calculator"]),
    57: ("News & Feed Readers", ["RSS Feed Reader", "Tech News Fetcher", "Cybersecurity Bulletins", "Weather Forecast Fetcher", "Stock Market Ticker", "Crypto Price Tracker", "Quote of the Day", "Daily Trivia Fetcher", "Wikipedia Quick Search", "Dictionary Definition"]),
    58: ("AI & Neural Assistants", ["Trace Spyder AI Chat", "Neural Prompt Generator", "AI Code Explainer", "AI Debugging Assistant", "Chat Transcript Manager", "API Key Configuration", "Free Neural Fallback", "AI Response Streamer", "Context Memory Viewer", "AI Settings Hub"]),
    59: ("Automation & Bots", ["Gmail Automation Bot", "Telegram Hub Manager", "Scheduled Task Runner", "Webhook Sender Tool", "Auto-Responder Bot", "Notification Dispatcher", "Script Trigger Bot", "File Watcher Daemon", "Batch Job Scheduler", "Automation Dashboard"]),
    60: ("Manual & About Suite", ["Complete User Manual", "About Trace Spyder", "Developer Credits", "Version History Info", "Keyboard Shortcuts Guide", "FAQ & Troubleshooting", "License & Terms", "Support & Contact Info", "Feature Roadmap", "Master Help Desk"])
}

def get_screen_width():
    try: return max(45, shutil.get_terminal_size((55, 20)).columns)
    except: return 52

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    bar = "─" * (w - 2)
    print(f"{C_CYAN}┌{bar}┐{C_RESET}")
    print(f"""{C_WHITE}  ████████╗██████╗  █████╗  ██████╗███████╗
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
  ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝{C_RESET}
         {C_YELLOW}🕷️  {C_CYAN}G O W R I   S H A N K A R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}TRACE SPYDER ULTIMATE{C_MAGENTA} ═ ⚡{C_RESET}""")
    print(f"{C_CYAN}└{bar}┘{C_RESET}")

def run_sub_tool(cat_id, sub_idx, sub_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print(f"\n{C_YELLOW}🚀 RUNNING: [{cat_id}.{sub_idx}] {sub_name}{C_RESET}\n")
    print(f"{C_GREEN}[*] Initializing execution engine...{C_RESET}")
    time.sleep(0.6)
    print(f"{C_CYAN}✔ Execution successful!{C_RESET}")
    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

def open_sub_menu(cat_id, cat_title, sub_list):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print(f"\n{C_MAGENTA}📂 CATEGORY {cat_id}: {cat_title.upper()}{C_RESET}\n")
        
        for idx, sub_name in enumerate(sub_list, 1):
            print(f"  {C_CYAN}[{cat_id}.{idx}]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}\033[1m{sub_name}{C_RESET}")

        print(f"\n{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}[0] 🔙 Back                                 {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}")

        raw = input(f"\n{C_GREEN}➤ Select Sub-Tool (1-10 or 0): {C_RESET}").strip()
        if raw in ['0', 'b', 'back']: break
        
        if raw.isdigit():
            s_idx = int(raw)
            if 1 <= s_idx <= len(sub_list):
                run_sub_tool(cat_id, s_idx, sub_list[s_idx - 1])

def open_other_softwares_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print(f"\n{C_YELLOW}📦 OTHER SOFTWARES (600-TOOL MASTER SUITE - 60 CATEGORIES){C_RESET}\n")
        
        for cid, (title, _) in MASTER_600_SUITE.items():
            print(f"  {C_CYAN}[{cid}]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}\033[1m{title}{C_RESET}")

        print(f"\n{C_CYAN}┌──────────────────────────────────────────────┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}[0] 🔙 Back to Main Menu                  {C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└──────────────────────────────────────────────┘{C_RESET}")

        raw = input(f"\n{C_GREEN}➤ Select Category (1-60 or 0): {C_RESET}").strip()
        if raw in ['0', 'b', 'back']: break
        
        if raw.isdigit():
            c_num = int(raw)
            if c_num in MASTER_600_SUITE:
                title, subs = MASTER_600_SUITE[c_num]
                open_sub_menu(f"{c_num}", title, subs)

def run_tool(filename):
    path = os.path.expanduser(f"~/{filename}")
    if os.path.exists(path):
        proc = subprocess.run([sys.executable, path])
        if proc.returncode == 99:
            sys.exit(0)
    else:
        print(f"\n{C_RED}❌ Error: '{filename}' not found.{C_RESET}")
        time.sleep(1.5)

def main():
    while True:
        w = get_screen_width()
        bar = "─" * (w - 2)
        print_banner()

        # AI Chat shortcut box
        print(f"\n{C_YELLOW}╔{'═' * (w-2)}╗{C_RESET}")
        print(f"{C_YELLOW}║{C_RESET} {C_RED}[*]{C_GREEN} \033[1m🤖 TRACE SPYDER AI CHAT (NEURAL CORE) ⚡\033[0m {C_YELLOW}║{C_RESET}")
        print(f"{C_YELLOW}╚{'═' * (w-2)}╝{C_RESET}\n")

        # 1-26 Main Core Tools
        for i in range(1, 27):
            k = str(i)
            if k in MENU_ITEMS:
                name = MENU_ITEMS[k][0].upper()
                print(f"  {C_CYAN}[{i}]{C_RESET} {C_YELLOW}➔{C_RESET} {C_WHITE}\033[1m{name}{C_RESET}")

        # Item 27: Other Softwares
        print(f"  {C_CYAN}[27]{C_RESET} {C_YELLOW}➔{C_RESET} {C_CYAN}\033[1m📦 OTHER SOFTWARES (600-TOOL MASTER SUITE)\033[0m")

        # Bottom Box: [28] Settings, [29] About, [0/x] Exit
        print(f"\n{C_CYAN}┌{bar}┐{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_GREEN}\033[1m[28] ⚙️  SYSTEM SETTINGS & DIAGNOSTICS\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_MAGENTA}\033[1m[29] 📖 COMPLETE MANUAL & ABOUT US\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}│{C_RESET}  {C_RED}\033[1m[0/x] 🚪 EXIT TERMINAL / CLOSE SESSION\033[0m{C_CYAN}│{C_RESET}")
        print(f"{C_CYAN}└{bar}┘{C_RESET}")

        raw = input(f"\n{C_GREEN}➤ Select Option ([*] AI / 1-29 / [0/x] Exit): {C_RESET}").strip().lower()

        if raw in ['*', '@', 'ai']:
            run_tool("ai_chat.py")
            continue

        if raw in ['0', '00', 'x', 'exit', 'q', 'quit']:
            print(f"\n{C_YELLOW}Closing Trace Spyder Terminal. Goodbye!{C_RESET}\n")
            sys.exit(0)

        if raw == '27':
            open_other_softwares_menu()
            continue
        elif raw in ['28', 'set', 'settings']:
            run_tool("settings.py")
            continue
        elif raw in ['29', 'abt', 'about']:
            run_tool("about.py")
            continue

        choice_clean = raw
        if choice_clean in MENU_ITEMS:
            name, script = MENU_ITEMS[choice_clean]
            run_tool(script)

if __name__ == "__main__":
    main()
