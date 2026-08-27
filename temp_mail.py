import os, sys, requests, time, random, string

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
         {C_YELLOW}🕷️  {C_CYAN}G O W R I   S H A N K A R{C_YELLOW}  🕷️{C_RESET}
           {C_MAGENTA}⚡ ═ {C_GREEN}T E R M I N A L   H U B{C_MAGENTA} ═ ⚡{C_RESET}
{C_CYAN}└────────────────────────────────────────────────────────────┘{C_RESET}"""

ACTIVE_MAIL_FILE = os.path.expanduser("~/.temp_active_mail.txt")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

DOMAINS = ["1secmail.com", "1secmail.org", "1secmail.net", "kzccv.com", "qiott.com", "wuuvo.com", "icznn.com"]

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(BANNER)
    print(f"{C_MAGENTA}  [▸] ACTIVE MODULE : {C_GREEN}TEMPORARY EMAIL & LIVE INBOX ENGINE{C_RESET}")
    print(f"{C_CYAN}─"*60 + f"{C_RESET}")

def get_current_email():
    if os.path.exists(ACTIVE_MAIL_FILE):
        with open(ACTIVE_MAIL_FILE, "r") as f:
            return f.read().strip()
    return None

def set_current_email(email_addr):
    with open(ACTIVE_MAIL_FILE, "w") as f:
        f.write(email_addr)

def generate_new_email():
    clear_screen()
    print(f"{C_YELLOW}[*] Generating secure disposable mailbox...{C_RESET}")
    
    # Generate random username and choose domain
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(DOMAINS)
    new_mail = f"{user}@{domain}"
    
    set_current_email(new_mail)
    print(f"\n{C_GREEN}✅ New Temp Email Generated Successfully!{C_RESET}")
    print(f"📧 Email Address: {C_WHITE}{new_mail}{C_RESET}")
    print(f"{C_YELLOW}ℹ️  Use this email anywhere. Incoming messages will appear in your inbox.{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to continue...{C_RESET}")

def view_inbox():
    while True:
        email_addr = get_current_email()
        if not email_addr:
            clear_screen()
            print(f"{C_RED}❌ No active Temp Email found! Please generate one first.{C_RESET}")
            input("\nPress Enter to continue...")
            return

        login, domain = email_addr.split("@")
        clear_screen()
        print(f"📧 Active Email : {C_GREEN}{email_addr}{C_RESET}")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"{C_YELLOW}[*] Checking for incoming messages (OTP / Verification)...{C_RESET}")

        messages = []
        try:
            url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
            res = requests.get(url, headers=HEADERS, timeout=8)
            if res.status_code == 200:
                messages = res.json()
        except Exception:
            pass

        print(f"\n{C_CYAN}╔══════════════════════ [ INBOX MESSAGES ] ══════════════════════╗{C_RESET}")
        if not messages:
            print(f"  {C_WHITE}📭 Inbox is empty. (Waiting for incoming emails...){C_RESET}")
        else:
            for idx, msg in enumerate(messages):
                print(f"  {C_YELLOW}[{idx+1}]{C_RESET} From: {C_WHITE}{msg['from'][:25]}{C_RESET} | Sub: {C_GREEN}{msg['subject'][:30]}{C_RESET} | Date: {msg['date']}")
        print(f"{C_CYAN}╚════════════════════════════════════════════════════════════════╝{C_RESET}")
        print(f"  {C_YELLOW}[0]{C_RESET} Refresh Inbox")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Temp Mail Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")

        c = input(f"{C_GREEN}➤ Select Mail Number to Read or Action ([0]/[#]): {C_RESET}").strip().lower()

        if c == '0':
            continue
        elif c in ['#', 'b', 'back']:
            break
        elif c in ['*', 'x', 'exit', 'q']:
            os._exit(0)
        elif c.isdigit() and 1 <= int(c) <= len(messages):
            msg_id = messages[int(c)-1]['id']
            read_message(login, domain, msg_id)

def read_message(login, domain, msg_id):
    clear_screen()
    try:
        url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
        res = requests.get(url, headers=HEADERS, timeout=8)
        if res.status_code == 200:
            m = res.json()
            print(f"{C_CYAN}╔══════════════════════ [ MESSAGE DETAILS ] ══════════════════════╗{C_RESET}")
            print(f"  {C_YELLOW}From   :{C_RESET} {m.get('from')}")
            print(f"  {C_YELLOW}Date   :{C_RESET} {m.get('date')}")
            print(f"  {C_YELLOW}Subject:{C_RESET} {C_GREEN}{m.get('subject')}{C_RESET}")
            print(f"{C_CYAN}─────────────────────────────────────────────────────────────────{C_RESET}")
            body = m.get('textBody') or m.get('body') or "[No Body Text Content]"
            print(f"{C_WHITE}{body}{C_RESET}")
            print(f"{C_CYAN}╚════════════════════════════════════════════════════════════════╝{C_RESET}")
        else:
            print(f"{C_RED}❌ Unable to read message content.{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Error: {e}{C_RESET}")
    input(f"\n{C_YELLOW}Press Enter to go back to inbox...{C_RESET}")

def main():
    while True:
        clear_screen()
        current = get_current_email()
        active_disp = f"{C_GREEN}{current}{C_RESET}" if current else f"{C_RED}None (Generate One){C_RESET}"
        print(f"  📧 Current Active Temp Mail : {active_disp}")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[1]{C_RESET} Generate New Disposable Email")
        print(f"  {C_CYAN}[2]{C_RESET} Open Live Inbox & Read Messages / OTPs")
        print(f"  {C_CYAN}[3]{C_RESET} Clear / Reset Current Mailbox")
        print(f"{C_CYAN}─"*60 + f"{C_RESET}")
        print(f"  {C_CYAN}[#]{C_RESET} Back to Main Hub Menu")
        print(f"  {C_RED}[*]{C_RESET} Full Exit to Terminal")
        print(f"{C_CYAN}═"*60 + f"{C_RESET}")

        c = input(f"{C_GREEN}➤ Option (1-3): {C_RESET}").strip().lower()
        if c == '1':
            generate_new_email()
        elif c == '2':
            view_inbox()
        elif c == '3':
            if os.path.exists(ACTIVE_MAIL_FILE):
                os.remove(ACTIVE_MAIL_FILE)
            print(f"\n{C_GREEN}✅ Temp mailbox reset!{C_RESET}")
            input("\nPress Enter to continue...")
        elif c in ['#', 'b', 'back']:
            break
        elif c in ['*', 'x', 'exit', 'q']:
            os._exit(0)

if __name__ == "__main__":
    main()