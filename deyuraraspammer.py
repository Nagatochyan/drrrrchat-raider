import requests
import threading
import random
import string
channelid = input(f'Thread code[The 5 degit code]: ')
naiyou=input(f'spamword:')
def qawqqq():
    codex = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    codex2= ''.join([random.choice(string.ascii_letters + string.digits) for i in range(12)])
    codex3= ''.join([random.choice(string.ascii_letters + string.digits) for i in range(7)])
    payload={
        "name":codex,
        "body":naiyou+codex2,
        "password":codex3
    }
    r = requests.post("http://general-bbs.drrrkari.com/api/v1/topics/"+channelid+"/posts", data=payload,headers={'User-Agent': 'Mozilla/5.0'})
    print(r)
while True:
    th1 = threading.Thread(target=qawqqq)
    th1.start()