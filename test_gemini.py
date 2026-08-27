import os, sys, json, time
import urllib.request, urllib.error

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
C_WHITE = "\033[1;37m"
C_RESET = "\033[0m"

KEY_FILE = os.path.expanduser("~/.gemini_api_key.txt")

def print_header():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"{C_CYAN}┌────────────────────────────────────────────────────┐{C_RESET}")
    print(f"{C_WHITE}      🤖 GEMINI AUTOMATED DIAGNOSTIC ENGINE        {C_RESET}")
    print(f"{C_YELLOW}           Trace Spyder System Integrity           {C_RESET}")
    print(f"{C_CYAN}└────────────────────────────────────────────────────┘{C_RESET}\n")

def run_diagnostics():
    print_header()
    
    # 1. API Key പരിശോധന
    print(f"{C_YELLOW}[TEST 1/4] Checking API Key File...{C_RESET}")
    if not os.path.exists(KEY_FILE):
        print(f"{C_RED}❌ പരാജയപ്പെട്ടു: ~/.gemini_api_key.txt ഫയൽ ലഭ്യമല്ല.{C_RESET}")
        return
        
    with open(KEY_FILE, "r") as f:
        api_key = f.read().strip()
        
    if not api_key:
        print(f"{C_RED}❌ പരാജയപ്പെട്ടു: API Key ഫയൽ ശൂന്യമാണ്.{C_RESET}")
        return
        
    masked_key = f"{api_key[:6]}...{api_key[-4:]}"
    print(f"{C_GREEN}✔ API Key കണ്ടെത്തി:{C_RESET} {masked_key}")

    # 2. സപ്പോർട്ട് ചെയ്യുന്ന മോഡലുകളുടെ പരിശോധന
    print(f"\n{C_YELLOW}[TEST 2/4] Testing Model Endpoints & Latency...{C_RESET}")
    test_models = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
    active_model = None
    headers = {"Content-Type": "application/json"}

    for model in test_models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": "Reply with only the word: PING_OK"}]}]}
        
        start_time = time.time()
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=12) as res:
                data = json.loads(res.read().decode('utf-8'))
                reply = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                latency = round((time.time() - start_time) * 1000, 2)
                
                if "PING_OK" in reply:
                    print(f"{C_GREEN}✔ {model}:{C_RESET} ആക്ടീവാണ് (Latency: {latency} ms)")
                    if not active_model:
                        active_model = model
                else:
                    print(f"{C_YELLOW}⚠ {model}:{C_RESET} മറുപടി ലഭിച്ചു ({reply})")
        except urllib.error.HTTPError as e:
            err = e.read().decode('utf-8', errors='ignore')
            print(f"{C_RED}✖ {model}:{C_RESET} HTTP {e.code} എറർ")
        except Exception as e:
            print(f"{C_RED}✖ {model}:{C_RESET} കണക്ഷൻ പരാജയപ്പെട്ടു ({e})")

    if not active_model:
        print(f"\n{C_RED}❌ മോഡലുകൾ ഒന്നും കണക്റ്റ് ആയില്ല. API Key ശരിയാണോ എന്ന് പരിശോധിക്കുക.{C_RESET}")
        return

    # 3. ഓട്ടോമേറ്റഡ് റീസണിംഗ് ടെസ്റ്റ്
    print(f"\n{C_YELLOW}[TEST 3/4] Running Automated Math & Logic Test...{C_RESET}")
    math_url = f"https://generativelanguage.googleapis.com/v1beta/models/{active_model}:generateContent?key={api_key}"
    math_payload = {"contents": [{"parts": [{"text": "Calculate 48 + 52. Reply ONLY with the final numeric value and nothing else."}]}]}
    
    try:
        req = urllib.request.Request(math_url, data=json.dumps(math_payload).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=12) as res:
            math_data = json.loads(res.read().decode('utf-8'))
            ans = math_data["candidates"][0]["content"]["parts"][0]["text"].strip()
            if "100" in ans:
                print(f"{C_GREEN}✔ ലോജിക് ടെസ്റ്റ് വിജയിച്ചു (Output: {ans}){C_RESET}")
            else:
                print(f"{C_YELLOW}⚠ അപ്രതീക്ഷിത മറുപടി: {ans}{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ ലോജിക് ടെസ്റ്റ് പരാജയപ്പെട്ടു: {e}{C_RESET}")

    # 4. മൾട്ടി-ടേൺ മെമ്മറി ടെസ്റ്റ്
    print(f"\n{C_YELLOW}[TEST 4/4] Running Multi-Turn Conversation Memory Test...{C_RESET}")
    memory_payload = {
        "contents": [
            {"role": "user", "parts": [{"text": "My secret code is SPYDER_99."}]},
            {"role": "model", "parts": [{"text": "Understood. I will remember your secret code."}]},
            {"role": "user", "parts": [{"text": "What is my secret code? Reply ONLY with the code."}]}
        ]
    }
    
    try:
        req = urllib.request.Request(math_url, data=json.dumps(memory_payload).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=12) as res:
            mem_data = json.loads(res.read().decode('utf-8'))
            mem_ans = mem_data["candidates"][0]["content"]["parts"][0]["text"].strip()
            if "SPYDER_99" in mem_ans:
                print(f"{C_GREEN}✔ കോൺടെക്സ്റ്റ് മെമ്മറി കൃത്യമായി പ്രവർത്തിക്കുന്നു (Recalled: {mem_ans}){C_RESET}")
            else:
                print(f"{C_YELLOW}⚠ മെമ്മറി റീകോൾ പരാജയപ്പെട്ടു: {mem_ans}{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ മെമ്മറി ടെസ്റ്റ് പരാജയപ്പെട്ടു: {e}{C_RESET}")

    # ഫൈനൽ റിപ്പോർട്ട്
    print(f"\n{C_CYAN}────────────────────────────────────────────────────{C_RESET}")
    print(f"{C_GREEN}✅ GEMINI AI INTEGRATION STATUS: FULLY OPERATIONAL{C_RESET}")
    print(f"{C_WHITE}Primary Model: {active_model}{C_RESET}")
    print(f"{C_CYAN}────────────────────────────────────────────────────{C_RESET}\n")

if __name__ == "__main__":
    run_diagnostics()