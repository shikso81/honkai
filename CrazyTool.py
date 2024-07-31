import os

    

import urllib.request
import json
import random  # Importing the random module
import threading
import requests

banner = """
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀▒
▒▒█▒▒███████▄██████▒▒▒
▒▒▒▒▒██████████████▒▒▒
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒

╔═╦═╦══╦══╦═╦╗ ╔══╦═╦═╦╗
║╔╣╬║╔╗╠══╠╗║║ ╚╗╔╣║║║║║
║╚╣╗╣╠╣║══╬╩╗║  ║║║║║║║╚╗
╚═╩╩╩╝╚╩══╩══╝  ╚╝╚═╩═╩═╝

┌───────────────────────────────────────────────────────────────────────────┐
│                 Разработчик: @Идёт нахуй асору лучше ТГК: @perehodasoru   │
│───────────────────────────────────────────────────────────────────────────│
│                               PREMIUM                                     │
└───────────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────────┬──────┐
│1. Поиск по номеру           10. Генератор карты                    │  V.4 │
│2. Поиск по IP               11. Генератор оскорблений              └──────┤
│3. Поиск по нику             12. Поиск по базе данных                      │
│4. DDOS                      13. Дизайнер                                  │
│5. Мануал по доксу           14. Св@т Б@нВ0рD                              │
│6. Сервисы                   15. ИИ кодер(beta)                            │
│7. Мануал по свату           16. Сообщить об ошибке софта                  │
│8. Мануал по сносу ТГ        17. Информация                                │
│9. Генератор личности        18. Выйти                                     │
└───────────────────────────────────────────────────────────────────────────┘



"""

print(banner)

choice = input("Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    os.system("python phone.py")

if choice == "2":
    os.system("clear")
    os.system("python ip.py")
    
if choice == "3":
    os.system("clear")
    os.system("python nick.py")

if choice == "4":
    os.system("clear")
    os.system("python ddos.py")

if choice == "5":
    os.system("clear")
    os.system("python doks.py")

if choice == "6":
   os.system("clear")
   os.system("python service.py")
   
if choice == "7":
    os.system("clear")
    os.system("python swat.py")

if choice == "8":
    os.system("clear")
    os.system("python snos.py")
    
if choice == "9":
    os.system("clear")
    os.system("python generate.py")

if choice == "10":
    os.system("clear")
    os.system("python card.py")

if choice == "11":
    os.system("clear")
    os.system("python troll.py")

if choice == "12":
    os.system("clear")
    os.system("python searchb.py")
    
if choice == "13":
    os.system("clear")
    os.system("python oform.py")
    
if choice == "14":
    os.system("python antispam.py")
    
if choice == "15":
    os.system("python ii.py")

if choice == "16":
    os.system("clear")
    os.system("python report.py")
if choice == "17":
    os.system("clear")
    os.system("python info.py")
if choice == "18":
    os.system("clear")
    os.system("python quit.py")
