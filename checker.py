import requests
import time

webhook = "webhook"
token = "token"
id = "id"
headers = {"authorization": token, "X-Audit-Log-Reason": "dc:berkrate", "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

session = requests.Session()
session.headers.update(headers)

def start():
    print(f"developed by berk' rate")
def urlalberk(berk_vanity):
    payload = {"code": berk_vanity}
    response = session.patch(f"https://canary.discord.com/api/v8/guilds/{id}/vanity-url", json=payload)

    if response.status_code == 429:
        print("Rate Limit")

    if response.status_code == 401:
        print("Token Yanlış")

    if response.status_code == 200:
        print(f"alindi : discord.gg/{berk_vanity} gg ez")
        
        data = {"content": f"discord.gg/{berk_vanity} :smile: ||@everyone||", "username": "berk rate checker"}
        requests.post(webhook, json=data)
    else:
        print(f"url alinamadi discord.gg/{berk_vanity} hata kodu : {response.status_code} | ")

def berkcheck(berk_vanity):
    response = session.get(f"https://canary.discord.com/api/v8/invites/{berk_vanity}")

    if response.status_code == 404:
        urlalberk(berk_vanity)

def urllist(filename, max_checks=200):
    with open(filename, 'r') as file:
        vanity_list = file.read().splitlines()

    checks = 0
    while checks < max_checks:
        for berk_vanity in vanity_list:
            berkcheck(berk_vanity)

            time.sleep(0.1)
            checks += 1
            if checks >= max_checks:
                break
            
if __name__ == "__main__":
    start()
    vanity_file = "vanity.txt"
    urllist(vanity_file)