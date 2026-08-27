import os, sys, time, subprocess

C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_RED = "\033[1;31m"
C_RESET = "\033[0m"

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{C_CYAN}--- AES ENCRYPTED VAULT ---{C_RESET}")
        print(" [1] Encrypt File\n [2] Decrypt File\n [0] Back")
        opt = input("\nSelect Option: ").strip().lower()
        if opt in ['0', 'b', 'x', 'm']: break
        if opt == '1':
            path = input("File to Encrypt: ").strip()
            if os.path.exists(path):
                pw = input("Password: ").strip()
                out_f = path + ".enc"
                subprocess.run(["openssl", "enc", "-aes-256-cbc", "-salt", "-pbkdf2", "-in", path, "-out", out_f, "-k", pw])
                print(f"{C_GREEN}Encrypted to {out_f}{C_RESET}")
                time.sleep(1)
        elif opt == '2':
            path = input("File to Decrypt (.enc): ").strip()
            if os.path.exists(path):
                pw = input("Password: ").strip()
                out_f = path.replace(".enc", ".dec")
                subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-in", path, "-out", out_f, "-k", pw])
                print(f"{C_GREEN}Decrypted to {out_f}{C_RESET}")
                time.sleep(1)

if __name__ == "__main__":
    main()
