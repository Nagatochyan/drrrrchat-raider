import requests
import threading
import random
import string


channelid = input(f'Thread name: ')
lolo = input(f'max thread[100 or 200]')
def qawsed():
    code1 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    codex = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
    codex2 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(12)])
    codex3 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(4)])
    payload = {
        "title": channelid+code1,
        "name": codex,
        "body": codex2,
        "password": codex3,
        "max_posts": int(lolo)
    }
    r = requests.post("http://general-bbs.drrrkari.com/api/v1/topics", data=payload,headers={'User-Agent': 'Mozilla/5.0'})
    print(r)
while True:
    th1 = threading.Thread(target=qawsed)
    th1.start()
