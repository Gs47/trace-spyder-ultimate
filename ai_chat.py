import os, sys, json, time, signal, re, shutil, textwrap
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import builtins

def safe_input(prompt=""):
    try:
        return _orig_input(prompt)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

_orig_input = builtins.input
builtins.input = safe_input

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

KEY_FILE = os.path.expanduser("~/.gemini_api_key.txt")
SESSIONS_FILE = os.path.expanduser("~/.spyder_ai_sessions.json")
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

def signal_handler(sig, frame):
    print(f"\n\n{C_YELLOW}[!] Operation canceled. Returning to prompt...{C_RESET}")

signal.signal(signal.SIGINT, signal_handler)

def get_screen_width():
    try:
        w = shutil.get_terminal_size((50, 20)).columns
        return max(34, w)
    except Exception:
        return 48

def print_banner(sub="TRACE SPYDER AI"):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = get_screen_width()
    inner_w = w - 2
    top_bar = "═" * inner_w

    logo_lines = [
        "████████╗██████╗  █████╗  ██████╗███████╗",
        "╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝",
        "   ██║   ██████╔╝███████║██║     █████╗  ",
        "   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ",
        "   ██║   ██║  ██║██║  ██║╚██████╗███████╗",
        "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝",
        "",
        "███████╗██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ",
        "██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗",
        "███████╗██████╔╝ ╚████╔╝ ██║  ██║█████╗  ██████╔╝",
        "╚════██║██╔═══╝   ╚██╔╝  ██║  ██║██╔══╝  ██╔══██╗",
        "███████║██║        ██║   ██████╔╝███████╗██║  ██║",
        "╚══════╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝"
    ]

    print(f"{C_CYAN}╔{top_bar}╗{C_RESET}")
    if w >= 50:
        for line in logo_lines:
            if not line: print(f"{C_CYAN}║{' ' * inner_w}║{C_RESET}")
            else: print(f"{C_CYAN}║{C_WHITE}{line.center(inner_w)}{C_CYAN}║{C_RESET}")
    else:
        c_title = "🕷️  TRACE SPYDER  🕷️"
        c_sub = "ULTIMATE TERMINAL SUITE"
        print(f"{C_CYAN}║{C_WHITE}{c_title.center(inner_w)}{C_CYAN}║{C_RESET}")
        print(f"{C_CYAN}║{C_CYAN}{c_sub.center(inner_w)}{C_CYAN}║{C_RESET}")

    author = "🕷️  G O W R I   S H A N K A R  🕷️"
    tag = f"⚡ ═ {sub} ═ ⚡"

    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{author.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║{C_MAGENTA}{tag.center(inner_w)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def load_sessions():
    if os.path.exists(SESSIONS_FILE):
        try:
            with open(SESSIONS_FILE, "r") as f: return json.load(f)
        except Exception: return {}
    return {}

def save_sessions(data):
    try:
        with open(SESSIONS_FILE, "w") as f: json.dump(data, f, indent=2)
    except Exception: pass

def get_api_key():
    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "r") as f:
                k = f.read().strip()
                if k: return k
        except Exception: pass
    return None

def stream_print_box(text, header_title=" TRACE SPYDER AI "):
    w = get_screen_width()
    inner_w = w - 4
    top_bar = "═" * (w - 2)

    print(f"\n{C_CYAN}╔{top_bar}╗{C_RESET}")
    print(f"{C_CYAN}║{C_YELLOW}{header_title.center(w - 2)}{C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╠{top_bar}╣{C_RESET}")

    paragraphs = str(text).split("\n")
    for p in paragraphs:
        p = p.rstrip()
        if not p.strip():
            print(f"{C_CYAN}║{' ' * (w - 2)}║{C_RESET}")
            continue

        wrapped = textwrap.wrap(p, width=inner_w, break_long_words=True, replace_whitespace=False)
        for line in wrapped:
            pad = inner_w - len(line)
            if pad < 0: pad = 0
            print(f"{C_CYAN}║ {C_WHITE}{line}{' ' * pad} {C_CYAN}║{C_RESET}")
            time.sleep(0.003)

    print(f"{C_CYAN}╚{top_bar}╝{C_RESET}")

def render_past_chat_transcript(messages):
    w = get_screen_width()
    div = "─" * (w - 2)
    print(f"\n{C_YELLOW}╔════ [ CONVERSATION TRANSCRIPT ] ════╗{C_RESET}")
    for msg in messages:
        role = msg.get("role", "user")
        text = msg.get("text", "")
        if role == "user":
            print(f"\n{C_GREEN}👤 [You]:{C_RESET} {C_WHITE}{text}{C_RESET}")
        else:
            print(f"\n{C_CYAN}🤖 [Trace Spyder AI]:{C_RESET}")
            wrapped = textwrap.wrap(text, width=w-4, break_long_words=True)
            for line in wrapped:
                print(f"   {C_WHITE}{line}{C_RESET}")
        print(f"{C_CYAN}{div}{C_RESET}")
    print(f"{C_GREEN}✅ Transcript loaded! You can now continue this session.{C_RESET}\n")

def manage_history_menu(sessions):
    w = get_screen_width()
    div = "─" * (w - 2)
    while True:
        print_banner("CHAT HISTORY MANAGER")
        if not sessions:
            print(f"\n{C_RED}  No past chat sessions found.{C_RESET}")
            print(f"  {C_CYAN}[0]{C_RESET} Back | {C_MAGENTA}[m]{C_RESET} Main | {C_RED}[x]{C_RESET} Exit")
            print(f"{C_CYAN}{div}{C_RESET}")
            inp = input(f"\n{C_GREEN}➤ Option: {C_RESET}").strip().lower()
            if inp in ['0', 'b', 'back']: return None
            elif inp in ['m', 'main']: sys.exit(0)
            elif inp in ['x', 'exit']: sys.exit(99)
            continue

        sorted_sessions = sorted(sessions.items(), key=lambda x: x[1].get("time", 0), reverse=True)
        for idx, (s_id, s_data) in enumerate(sorted_sessions, 1):
            title = s_data.get("title", "Conversation")[:w-18]
            msg_cnt = len(s_data.get("messages", []))
            print(f"  {C_CYAN}[{idx:02d}]{C_RESET} {C_WHITE}{title:<24}{C_RESET} {C_YELLOW}({msg_cnt} msgs){C_RESET}")

        print(f"\n  {C_CYAN}[0]{C_RESET} Back  |  {C_GREEN}[d <num>]{C_RESET} Delete One (e.g. d 1)  |  {C_RED}[clear]{C_RESET} Wipe All")
        print(f"{C_CYAN}{div}{C_RESET}")

        choice = input(f"\n{C_GREEN}➤ Select Option or Session Number: {C_RESET}").strip().lower()
        if choice in ['0', 'b', 'back']: return None
        elif choice in ['m', 'main']: sys.exit(0)
        elif choice in ['x', 'exit']: sys.exit(99)
        elif choice == 'clear':
            sessions.clear()
            save_sessions(sessions)
            print(f"{C_GREEN}✔ All chat histories wiped successfully!{C_RESET}")
            time.sleep(1)
            return None
        elif choice.startswith('d ') or choice.startswith('delete '):
            parts = choice.split()
            if len(parts) == 2 and parts[1].isdigit():
                idx_to_del = int(parts[1]) - 1
                if 0 <= idx_to_del < len(sorted_sessions):
                    del_id, del_data = sorted_sessions[idx_to_del]
                    del sessions[del_id]
                    save_sessions(sessions)
                    print(f"{C_GREEN}✔ Session '{del_data.get('title')}' deleted!{C_RESET}")
                    time.sleep(1.2)
                else:
                    print(f"{C_RED}❌ Invalid session number.{C_RESET}")
                    time.sleep(1)
            continue
        
        if choice.isdigit() and 1 <= int(choice) <= len(sorted_sessions):
            return sorted_sessions[int(choice) - 1][0]
    return None

def query_gemini_api(prompt, history_messages, api_key):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        contents = []
        for m in history_messages[-6:]:
            r = "user" if m["role"] == "user" else "model"
            contents.append({"role": r, "parts": [{"text": m["text"]}]})
        contents.append({"role": "user", "parts": [{"text": prompt}]})

        res = requests.post(url, json={"contents": contents}, headers={'Content-Type': 'application/json'}, timeout=12)
        if res.status_code == 200:
            return res.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception: pass
    return None

def query_pollinations(history_messages, prompt):
    try:
        url = "https://text.pollinations.ai/"
        system_msg = "You are Trace Spyder AI by Gowri Shankar. Maintain context seamlessly with clear bullet points."
        messages = [{"role": "system", "content": system_msg}]
        for msg in history_messages[-6:]:
            role = "user" if msg["role"] == "user" else "assistant"
            messages.append({"role": role, "content": str(msg["text"])})
        messages.append({"role": "user", "content": str(prompt)})

        res = requests.post(url, json={"messages": messages, "model": "openai"}, headers=HEADERS, timeout=12)
        if res.status_code == 200 and res.text.strip(): return res.text.strip()
    except Exception: pass
    return None

def query_live_web_search(prompt):
    clean_term = re.sub(r'(?i)\b(who is|what is|tell me about|explain|website)\b', '', prompt).strip() or prompt.strip()
    try:
        res = requests.post(f"https://html.duckduckgo.com/html/?q={requests.utils.quote(clean_term)}", data={'q': clean_term}, headers=HEADERS, timeout=8)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            results = [s.text.strip() for s in soup.find_all('a', class_='result__snippet') if s.text.strip()][:3]
            if results: return f"[Web Intelligence for '{clean_term}']:\n\n• " + "\n\n• ".join(results)
    except Exception: pass
    return None

def main():
    api_key = get_api_key()
    sessions = load_sessions()
    active_session_id = str(int(time.time()))
    sessions[active_session_id] = {
        "title": "New Chat Session",
        "date": datetime.now().strftime("%d %b, %H:%M"),
        "time": time.time(),
        "messages": []
    }

    while True:
        try:
            w = get_screen_width()
            div = "─" * (w - 2)
            print_banner("NEURAL CORE")
            curr_messages = sessions[active_session_id]["messages"]
            
            print(f"  {C_MAGENTA}[▸] SESSION :{C_RESET} {C_WHITE}{sessions[active_session_id]['title'][:w-18]}{C_RESET}")
            print(f"  {C_YELLOW}[hist]{C_RESET} History | {C_GREEN}[new]{C_RESET} New | {C_MAGENTA}[m]{C_RESET} Main | {C_RED}[x]{C_RESET} Exit")
            print(f"{C_CYAN}{div}{C_RESET}")

            prompt = input(f"\n{C_GREEN}➤ Ask / Continue: {C_RESET}").strip()
            if not prompt: continue

            cmd = prompt.lower()
            if cmd in ['0', '00', 'b', 'back', '#']: break
            elif cmd in ['m', 'main', 'home']: sys.exit(0)
            elif cmd in ['x', 'exit', 'q', 'quit']: sys.exit(99)
            elif cmd in ['hist', 'history', 'h']:
                chosen_id = manage_history_menu(sessions)
                if chosen_id and chosen_id in sessions:
                    active_session_id = chosen_id
                    print_banner("RESUMED CHAT")
                    render_past_chat_transcript(sessions[active_session_id]["messages"])
                    input(f"{C_GREEN}Press Enter to continue chatting...{C_RESET}")
                continue
            elif cmd in ['new', 'clear']:
                active_session_id = str(int(time.time()))
                sessions[active_session_id] = {
                    "title": "New Chat Session",
                    "date": datetime.now().strftime("%d %b, %H:%M"),
                    "time": time.time(),
                    "messages": []
                }
                save_sessions(sessions)
                continue

            if not curr_messages:
                sessions[active_session_id]["title"] = prompt[:24]

            print(f"\n{C_YELLOW}[*] Processing with context continuation...{C_RESET}")
            response = None
            if api_key: response = query_gemini_api(prompt, curr_messages, api_key)
            if not response: response = query_pollinations(curr_messages, prompt)
            if not response: response = query_live_web_search(prompt)

            if response:
                sessions[active_session_id]["messages"].append({"role": "user", "text": prompt})
                sessions[active_session_id]["messages"].append({"role": "assistant", "text": response})
                sessions[active_session_id]["time"] = time.time()
                save_sessions(sessions)
                stream_print_box(response)
            else:
                print(f"\n{C_RED}❌ Connection issue. Please try again.{C_RESET}")

            inp = input(f"\n{C_GREEN}Enter to continue ([0] Back / [m] Main / [x] Exit): {C_RESET}").strip().lower()
            if inp in ['0', 'b', 'back']: break
            elif inp in ['m', 'main']: sys.exit(0)
            elif inp in ['x', 'exit']: sys.exit(99)

        except Exception as e:
            print(f"\n{C_RED}[!] Recovered: {e}{C_RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
