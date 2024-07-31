import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests
import faker

fake = faker.Faker(locale="ru_RU")
gender = input("\n[?] Введите пол (М - мужской, Ж - женский -> ")
print()
if gender not in ["М", "Ж"]:
    gender = random.choice(["М", "Ж"])
    print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n")
if gender == "М":
    first_name = fake.first_name_male()
    middle_name = fake.middle_name_male()
else:
    first_name = fake.first_name_female()
    middle_name = fake.middle_name_female()
last_name = fake.last_name()
full_name = f"{last_name} {first_name} {middle_name}"
birthdate = fake.date_of_birth()
age = fake.random_int(min=18, max=80)
street_address = fake.street_address()
city = fake.city()
region = fake.region()
postcode = fake.postcode()
address = f"{street_address}, {city}, {region} {postcode}"
email = fake.email()
phone_number = fake.phone_number()
inn = str(fake.random_number(digits=12, fix_len=True))
snils = str(fake.random_number(digits=11, fix_len=True))
passport_num = str(fake.random_number(digits=10, fix_len=True))
passport_series = fake.random_int(min=1000, max=9999)
print(f"[+] ФИО: {full_name}\n")
print(f"[+] Пол: {gender}\n")
print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n")
print(f"[+] Возраст: {age} лет\n")
print(f"[+] Адрес: {address}\n")
print(f"[+] Email: {email}\n")
print(f"[+] Телефон: {phone_number}\n")
print(f"[+] ИНН: {inn}\n")
print(f"[+] СНИЛС: {snils}\n")
print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n")
back = input("[?] Вернуться в главное меню? Yes/No -> ")

if back == "Yes":
    os.system("clear")
    os.system("python main.py")
if back == "No":
    print("[!] Хорошо, вы не вернетесь в главное меню ")
