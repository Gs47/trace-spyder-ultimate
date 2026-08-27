import os, sys, shutil, time

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

TOOL_DOCS = [
    ("Trace Spyder AI Chat", "ai_chat.py", "AI & Automation", "Intelligent terminal assistant powered by neural models.", "• Fluent multilingual reasoning.\n• Multi-turn conversational memory recall.\n• Live word streaming response engine."),
    ("Gmail Automation Bot", "gmail_bot.py", "AI & Automation", "Terminal CLI to dispatch emails and inspect inbox.", "• Secure authentication with Google App Passwords.\n• 1-Click unread email inspection.\n• Instant email dispatch engine."),
    ("Telegram Hub Manager", "tg_manager.py", "AI & Automation", "Manage Telegram bots, broadcasts, and media channels.", "• Broadcast messages via Bot API.\n• Channel updates and file distribution."),
    ("Universal Media Downloader", "media_dl.py", "Downloaders", "Download high-res media from YouTube, IG, Facebook, etc.", "• Up to 4K video downloads and 320kbps MP3 extractions.\n• Powered by robust yt-dlp core."),
    ("Spotify Music Downloader", "spotify_dl.py", "Downloaders", "Download high-quality audio tracks directly.", "• Convert track links to MP3 format.\n• Embeds metadata and album artwork."),
    ("TeraBox Cloud Downloader", "terabox_dl.py", "Downloaders", "Download files directly without the mobile app.", "• Generates direct high-speed cloud download URLs."),
    ("Web Page & Asset DL", "web_dl.py", "Downloaders", "Download web pages and all linked assets locally.", "• Archive web assets, images, and source code for offline use."),
    ("Audio/Video Converter", "converter.py", "Media Utilities", "Convert between media container formats.", "• Supports MP4 to MP3, MKV to MP4, PNG to JPG.\n• Powered by high-speed FFmpeg encoder."),
    ("OSINT Target Recon", "recon_tool.py", "Recon & OSINT", "Open Source Intelligence investigation framework.", "• Username tracking across 100+ social platforms.\n• Digital footprint mapping."),
    ("Web Domain Recon", "web_recon.py", "Recon & OSINT", "Inspect target DNS records, SSL certs, and HTTP headers.", "• Discover web security headers and server technology stacks."),
    ("Network Audit & Scan", "net_tools.py", "Network Security", "Local network auditing, IP lookup, and port scanning.", "• Discover connected LAN devices.\n• Open port scanner and latency benchmarks."),
    ("Seeker Location Engine", "seeker_hub.py", "Location Recon", "High-accuracy geolocation reconnaissance tool.", "• Device-permitted GPS coordinates lookup."),
    ("Phone Number Lookup", "check_number.py", "Recon & OSINT", "Analyze carrier, country code, and format validation.", "• International phone numbering validation."),
    ("AES Encrypted Vault", "file_vault.py", "Security & Privacy", "Military-grade AES encryption for sensitive files.", "• Password-protected secure file vault."),
    ("Cryptography & Ciphers", "crypto_tool.py", "Security & Privacy", "Classic and modern cryptographic cipher suite.", "• Caesar, Vigenere, ROT13, and custom ciphers."),
    ("Hash Generator & Check", "hash_tool.py", "Security & Privacy", "Generate and verify MD5, SHA-1, and SHA-256 hashes.", "• Validate software and file payload integrity."),
    ("Multi-Base Encoder", "encoder_tool.py", "Security & Privacy", "Encode and decode Base64, Hex, URL, and Binary strings.", "• Rapid conversion for obfuscated payloads."),
    ("Secure Password Gen", "pwgen_tool.py", "Security & Privacy", "Generate cryptographically secure passwords.", "• Customizable length and character sets."),
    ("Disposable Temp Mail", "temp_mail.py", "Security & Privacy", "Generate temporary disposable inboxes.", "• Ideal for OTPs and verification tokens."),
    ("Link Unshortener", "link_unshort.py", "Security & Privacy", "Trace redirect chains without opening suspicious URLs.", "• Safeguards against malicious phishing links."),
    ("Device Hardware Info", "device_info.py", "System Utilities", "Telemetry on RAM, CPU, battery, and storage.", "• Full device hardware specification audit."),
    ("Phone Storage Cleaner", "phone_cleaner.py", "System Utilities", "Wipe cache, thumbnails, and temp files.", "• Reclaim storage and enhance terminal responsiveness."),
    ("System Benchmark", "benchmark_tool.py", "System Utilities", "Benchmark CPU floating-point calculations.", "• Single-core and multi-threaded stress benchmarks."),
    ("Zip Master Utility", "zip_master.py", "System Utilities", "Manage ZIP, TAR, and GZ archives.", "• Create and extract encrypted archives."),
    ("QR Code Maker/Scan", "qr_tool.py", "System Utilities", "Generate and read terminal QR codes.", "• ASCII QR code render engine."),
    ("Terminal Quick Notes", "notes_tool.py", "System Utilities", "Encrypted quick notes vault.", "• Local note management from the CLI."),
    ("Multi-Engine Search", "search_engine.py", "System Utilities", "Direct command-line multi-engine search.", "• Ad-free search via DuckDuckGo and Wikipedia."),
    ("System Settings & Diagnostics", "settings.py", "Core & Diagnostics", "System configuration and automated audit suite.", "• 10 central maintenance and audit hubs.")
]

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{C_CYAN}┌────────────────────────────────────────────────────────────┐
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
  ╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝{C_RESET}
         {C_YELLOW}🕷️  {C_CYAN}G O W R I   S H A N K A R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}T R A C E   S P Y D E R   A I{C_MAGENTA} ═ ⚡{C_RESET}
{C_CYAN}└────────────────────────────────────────────────────────────┘{C_RESET}""")

def show_all_manual():
    print_banner()
    print(f"{C_YELLOW}─── [ 📚 ALL MODULES COMPLETE MANUAL ] ───{C_RESET}\n")

    for idx, (name, fname, cat, short_d, long_d) in enumerate(TOOL_DOCS, 1):
        print(f"{C_CYAN}[{idx:02d}] {C_WHITE}{name}{C_RESET} {C_MAGENTA}[{fname}]{C_RESET}")
        print(f"{C_YELLOW}Category:{C_RESET} {cat}")
        print(f"{C_WHITE}Overview:{C_RESET} {short_d}")
        print(f"{C_GREEN}Features:{C_RESET}\n{long_d}")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}\n")
        if idx % 4 == 0:
            ch = input(f"{C_YELLOW}Press Enter to continue (or [0] to go back): {C_RESET}").strip()
            if ch in ['0', 'b', 'back', '#']:
                return

    input(f"\n{C_GREEN}Press Enter or [0] to return...{C_RESET}")

def search_tool():
    print_banner()
    query = input(f"{C_GREEN}➤ Enter tool name to search: {C_RESET}").strip().lower()
    if not query or query in ['0', 'b', 'back', '#']: return

    found = False
    for idx, (name, fname, cat, short_d, long_d) in enumerate(TOOL_DOCS, 1):
        if query in name.lower() or query in fname.lower() or query in cat.lower():
            found = True
            print(f"\n{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")
            print(f"{C_WHITE}▪ Module Name:{C_RESET} {C_GREEN}{name}{C_RESET} ({fname})")
            print(f"{C_WHITE}▪ Category   :{C_RESET} {C_MAGENTA}{cat}{C_RESET}")
            print(f"{C_WHITE}▪ Overview   :{C_RESET} {short_d}")
            print(f"{C_WHITE}▪ Features   :{C_RESET}\n{long_d}")
            print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

    if not found:
        print(f"\n{C_RED}❌ No matching documentation found for '{query}'.{C_RESET}")

    input(f"\n{C_GREEN}Press Enter to return...{C_RESET}")

def main():
    while True:
        print_banner()
        print(f" {C_CYAN}1.{C_RESET} 📖 Complete User Manual (All 28 Modules)")
        print(f" {C_CYAN}2.{C_RESET} 🔍 Search Tool Documentation & Features")
        print(f" {C_CYAN}0.{C_RESET} 🔙 Back to Main Menu")
        print(f"{C_CYAN}────────────────────────────────────────────────────────────{C_RESET}")

        choice = input(f"\n{C_GREEN}➤ Select Option: {C_RESET}").strip()

        if choice == '1':
            show_all_manual()
        elif choice == '2':
            search_tool()
        elif choice in ['0', '00', '#', 'b', 'back', 'exit', 'q']:
            break

if __name__ == "__main__":
    main()