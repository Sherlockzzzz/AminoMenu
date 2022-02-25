import os
import sys
import colorama
import time
from time import sleep
from colorama import init, Fore, Back
init(autoreset=True)
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN + "Welcome!" , Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN +  "" + ' ', Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN +  "",  Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN +  "",  Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN +  "", Back.GREEN + '')
print(Back.GREEN + '', Fore.GREEN +  "" + '    ', Back.GREEN + '')
print()
print()
print(Back.GREEN + '', Fore.GREEN + "       Version - 0.1.0       ", Back.GREEN + '')
print(Back.GREEN + '', " =============================================", Back.GREEN + '')
print(Back.GREEN + '', "        Made by", Fore.CYAN + "Sherlock                " + '      ', Back.GREEN + '')
print(Back.GREEN + '', "        Updates:", Fore.CYAN + "https://t.me/hranitel_madara_kanal" + '      ', Back.GREEN + '')
print(Back.GREEN + '', " =============================================", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.YELLOW  + """     \               _)                 \  |                     
    _ \    __ `__ \   |  __ \    _ \   |\/ |   _ \  __ \   |   | 
   ___ \   |   |   |  |  |   |  (   |  |   |   __/  |   |  |   | 
 _/    _\ _|  _|  _| _| _|  _| \___/  _|  _| \___| _|  _| \__._| 
                                                                 
""" + '                 ', Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + '      ' + Back.RED + '!' + Back.BLACK + '                ' + Back.BLACK + '                        ' + Back.GREEN + "")
print(Back.GREEN + '', Fore.LIGHTMAGENTA_EX  + "      1.[Трансфер]       2.[Рейд-Бот]       3.[Информация]" + '', Back.GREEN + '')
print(Back.GREEN + '', Back.BLACK + "                                              ", Back.GREEN + '')
print(Back.GREEN + '', Fore.MAGENTA  + "         '''''''''''''''''''''''''''''''''''''''''''' ", Back.GREEN + '')

inp = int(input(">>"))
if inp == 1:
            print(Fore.GREEN + 'Вы выбрали [Трансфер]!')
            import os
            os.system("pip install samino==1.8.8")
            os.system("pip install pyfiglet")
            os.system("pip install colorama")
            import samino,threading, json
            from os import path
            import pyfiglet
            from colorama import init, Fore, Style
            from concurrent.futures import ThreadPoolExecutor
            init()
            print("""────┈┈┈┄┄╌╌╌╌┄┄┈┈┈┈┈┈┄┄╌╌╌╌┄┄┈┈┈────""")
            print((f"""{pyfiglet.figlet_format("❮ Transfer VIP ❯", font="standard")}"""))
            print("""────┈┈┈┄┄╌╌╌╌┄┄┈┈┈┈┈┈┄┄╌╌╌╌┄┄┈┈┈────""")
            Chose = int(input("""
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┫      •Трансфер Фан-Клуб•          ┃
            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            ┣• 1 - Передать монеты с ОДНОГО аккаунта
            ┃────────────────────────────── ─ ━┃
            ┣• 2 - Перевести со всех аккаунтов в .json файле
            ┗┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>  """))
            print("""────┈┈┈┄┄╌╌╌╌┄┄┈┈┈┈┈┈┄┄╌╌╌╌┄┄┈┈┈────""")
            url = input("Ссылку на Фан-Клуб >> ")
            print("""────┈┈┈┄┄╌╌╌╌┄┄┈┈┈┈┈┈┄┄╌╌╌╌┄┄┈┈┈────""")
            if Chose == 1:
                client = samino.Client()
                Choose = int(input("""
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┏┫      •Авторизация•     ┃
                ┃┣━━━━━━━━━━━━━━━━━━━━━━━━━┛
                ┃┣• 1 - Почта и пароль
                ┃┃───────────────────── ─ ━
                ┃┣• 2 - SID
                ┃┃───────────────────── ─ ━
                ┃┃>> """))
                if Chose == 1:
                    Email = input("Почта >> ")
                    Password = input("Пароль >> ")
                    client.login(Email, Password)
                    if Choose == 2:
                        SID = input(" SID >> ")
                        client.sid_login(sid=SID)
                        if Choose != (1,2):
                            print("Пожалуйста, выберете между 2 и 1! ")
                            coins = client.get_wallet_info().totalCoins
                            print(f"Your coins = {coins} \n")
                            c = int(input("Сколько монет перевести >>  "))
                            total = 0
                            path = client.get_from_link(url)
                            comId = path.comId
                            userId = path.objectId
                            client.join_community(comId)
                            local = samino.Local(comId)
                            fee = int(local.get_user_info(userId).influencerMonthlyFee)
                            if fee > c: print(f"VIP Subscription Coins is {fee}\nyou choosed {c}")
                            for _ in range(int(c / fee)):
                                threading.Thread(target=local.subscribe, args=(userId, )).start()
                                coins -= 500
                                print("500 переведено")
                                total += 500
                                if coins < 500:
                                    break
                                print(f"Вы перевели {total} монет")
                                if Chose == 2:
                                    THIS_FOLDER = path.dirname(path.abspath(__file__))
                                    emailfile=path.join(THIS_FOLDER,"accounts.json")
                                    dictlist=[]
                                    with open(emailfile) as f:
                                        dictlist = json.load(f)
                                        def log(cli : samino.Client,email : str, password : str):
                                            Exception
print()
pass
def threadit(acc : dict):
    email=acc["email"]
    password=acc["password"]
    device=acc["device"]
    client=samino.Client(deviceId=device)
    log(cli=client,email=email,password=password);print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print(f"Зарегистрирован {email}")
    path = client.get_from_link(url)
    comId = path.comId
    userId = path.objectId
    client.join_community(comId)
    local = samino.Local(comId)
    coins = client.get_wallet_info().totalCoins
    print(f"Монет на аккаунте = {coins} \n")
    if coins == 500:
        c = ("500")
        if coins > 500 :
            c = ("500")
            if coins < 500 :
                c = coins
                fee = int(local.get_user_info(userId).influencerMonthlyFee)
                if fee > c: print(f"VIP Subscription Coins is {fee}\nyou choosed {c}")
                total = 0
                for _ in range(int(c / fee)):
                    threading.Thread(target=local.subscribe, args=(userId, )).start()
                    coins -= 500
                    print(f"Done {_} > {fee}")
                    total += 500    
                    def main():
                        print(f"\n\33[48;5;5m\33[38;5;234m ❮ {len(dictlist)} ACCOUNTS LOADED ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")
                        for amp in dictlist:
                            threadit(amp)
                            print(f"\n\n\33[48;5;5m\33[38;5;234m ❮ Transferred all coins from {len(dictlist)} ACCOUNTS ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")
                            if __name__ == '__main__':
                                main()
                                if Chose != (1,2):
                                    print("Пожалуйста, выберете между 2 и 1!")
if inp == 2:                                                                                  
    print(Fore.GREEN + 'Вы выбрали [Рейд-Бот]!')
    print(""" [1] - Спам в чаты 

 [2] - В разработке""")
    menu = int(input(">> "))
    if menu == 1:
        print("     • Спам В Чаты •  ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        email = str(input("Почта >> "))
        password = str(input("Пароль >> "))
        message = str(input("Текст >> "))
        link = str(input("Ссылка на чат >> "))
        import threading
        import amino
        client = amino.Client()
        client.login(email, password)
        code = client.get_from_code(link)
        ndcId = code.json["extensions"]["linkInfo"]["ndcId"]
        subclient = amino.SubClient(ndcId, profile=client.profile)
        chatId = code.json["extensions"]["linkInfo"]["objectId"]
        def spam():
            while True:
                subclient.send_message(chatId, message, 109)
                for _ in range(100):
                    threading.Thread(target=spam).start()
if inp == 3:
    print(Fore.GREEN + 'Вы выбрали [Информация]!')
    print("""
    [1] - Создатели  
    [2] -  Как пользоваться
    [3] - О Амино  """)
    help = input(">>")
    if help == "1":
        print("            <<Создатели>>         ")
        print("""
        Sherlock - Создатель этого меню, оформления, перевода. (Программист Python)
        wzhxycl - Создатель скрипта Рейд-Бот постами(программист Python)
        3loy - создатель скрипта трансфер(программист Python
        Madara - Помощник(помощник) """)
        print("[1] - Назад.")
        ach = input(">>")
        if help == "2":
                print("   В разработке. . .")
                if help == "3":
                    print("Амино — это сеть тематических сообществ. Приложение и большая социальная сеть на его базе. Это отличное место, где люди с общими интересами могут собраться вместе и поговорить о чем угодно. Адрес: aminoapps.com/explore/ru. Пользоваться Амино можно и через браузер на обычном ПК. Чтобы создатьсообщество вам надо поставить приложение на мобильное устройство. Внутри множество тематических сообществ.")
                    
                        
