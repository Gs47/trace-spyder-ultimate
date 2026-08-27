import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, sys, json, time

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


CONFIG_FILE = os.path.expanduser("~/.gmail_creds.json")

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

def load_creds():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return None
    return None

def save_creds(email_addr, app_pw):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"email": email_addr, "password": app_pw}, f)

def send_email(sender, app_pw, to_addr, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        print(f"\n{C_YELLOW}[*] Connecting to Gmail SMTP server...{C_RESET}")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, app_pw)
        server.send_message(msg)
        server.quit()
        print(f"{C_GREEN}✅ ഇമെയിൽ വിജയകരമായി അയച്ചു ({to_addr})!{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ അയക്കാൻ കഴിഞ്ഞില്ല: {e}{C_RESET}")

def read_unread_emails(sender, app_pw):
    try:
        print(f"\n{C_YELLOW}[*] Connecting to Gmail IMAP server...{C_RESET}")
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(sender, app_pw)
        mail.select('inbox')

        status, messages = mail.search(None, 'UNSEEN')
        mail_ids = messages[0].split()

        if not mail_ids:
            print(f"{C_GREEN}✅ പുതിയ (Unread) ഇമെയിലുകൾ ഒന്നുമില്ല.{C_RESET}")
            return

        print(f"{C_GREEN}📩 പുതിയ {len(mail_ids)} ഇമെയിലുകൾ കണ്ടെത്തി:{C_RESET}\n")

        for mid in mail_ids[-5:]:
            _, msg_data = mail.fetch(mid, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    sub = msg.get('Subject', 'No Subject')
                    from_ = msg.get('From', 'Unknown Sender')
                    print(f"{C_CYAN}From:{C_RESET} {from_}")
                    print(f"{C_YELLOW}Subject:{C_RESET} {sub}")
                    print(f"{C_CYAN}──────────────────────────────────────{C_RESET}")
        mail.close()
        mail.logout()
    except Exception as e:
        print(f"{C_RED}❌ മെയിലുകൾ പരിശോധിക്കാൻ കഴിഞ്ഞില്ല: {e}{C_RESET}")

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"{C_CYAN}┌────────────────────────────────────────────────────┐{C_RESET}")
    print(f"{C_WHITE}        📧 TRACE SPYDER - GMAIL AUTOMATION          {C_RESET}")
    print(f"{C_CYAN}└────────────────────────────────────────────────────┘{C_RESET}")

    creds = load_creds()
    if not creds:
        print(f"{C_YELLOW}[!] Gmail ലോഗിൻ വിവരങ്ങൾ ആവശ്യമാണ്:{C_RESET}")
        user_email = input(f"{C_GREEN}➤ നിങ്ങളുടെ Gmail ID: {C_RESET}").strip()
        app_pw = input(f"{C_GREEN}➤ 16-Digit App Password: {C_RESET}").strip().replace(" ", "")
        if user_email and app_pw:
            save_creds(user_email, app_pw)
            creds = {"email": user_email, "password": app_pw}
        else:
            print(f"{C_RED}ഡാറ്റ അപൂർണ്ണമാണ്.{C_RESET}")
            return

    while True:
        print(f"\n{C_CYAN}1.{C_RESET} പുതിയ ഇമെയിൽ അയക്കുക (Send Mail)")
        print(f"{C_CYAN}2.{C_RESET} വായിക്കാത്ത ഇമെയിലുകൾ പരിശോധിക്കുക (Check Unread)")
        print(f"{C_CYAN}3.{C_RESET} ലോഗിൻ വിവരങ്ങൾ മാറ്റുക (Reset Credentials)")
        print(f"{C_CYAN}0.{C_RESET} തിരികെ പോകുക (Exit)")

        choice = input(f"\n{C_GREEN}➤ Option തിരഞ്ഞെടുക്കുക: {C_RESET}").strip()

        if choice == '1':
            to = input(f"{C_GREEN}To (സ്വീകർത്താവിന്റെ Email): {C_RESET}").strip()
            subject = input(f"{C_GREEN}Subject (വിഷയം): {C_RESET}").strip()
            print(f"{C_GREEN}Message Body (സന്ദേശം ടൈപ്പ് ചെയ്യുക):{C_RESET}")
            body = input("➤ ")
            send_email(creds["email"], creds["password"], to, subject, body)
        elif choice == '2':
            read_unread_emails(creds["email"], creds["password"])
        elif choice == '3':
            if os.path.exists(CONFIG_FILE): os.remove(CONFIG_FILE)
            print(f"{C_GREEN}ലോഗിൻ ക്ലിയർ ചെയ്തു. ആപ്പ് റീസ്റ്റാർട്ട് ചെയ്യുക.{C_RESET}")
            break
        elif choice in ['0', '#', 'b', 'back', 'exit']:
            break

if __name__ == "__main__":
    main()