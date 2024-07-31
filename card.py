import urllib.request
import json
import os
import random  # Importing the random module
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
        "CVV": cvv
    }

card = generate_random_card(country)
print("\n[!] Страна: " + card["Страна"])
print("\n[!] Номер карты: " + card["Номер карты"])
print("\n[!] Срок действия: " + card["Срок действия"])
print("\n[!] CVV: " + card["CVV"] + "\n")

back = input("[?] Вернуться в главное меню? Yes/No -> ")

if back == "Yes":
    os.system("clear")
    os.system("python main.py")
if back == "No":
    print("[!] Хорошо, вы не вернетесь в главное меню ")
