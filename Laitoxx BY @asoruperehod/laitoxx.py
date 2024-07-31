import os
import time
import ctypes
from ctypes import wintypes
from datetime import datetime, timedelta
import re
import socket
import subprocess
import sys
import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import whois
import colorama
from colorama import Fore, init
from pystyle import Anime, Colors, Colorate, Center

class Color:
    DARK_RED = '\033[31m'
    DARK_GRAY = '\033[90m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


LIGHT_RED = '\033[91m'
RED = '\033[91m'
DARK_RED = '\033[31m'
DARK_GRAY = '\033[90m'
GRAY = '\033[37m'
RESET = '\033[0m'


def gradient_text(text):
    gradient_colors = [
        LIGHT_RED,
        RED,
        DARK_RED,
        DARK_GRAY,
        GRAY
    ]

    num_colors = len(gradient_colors)
    gradient_steps = len(text) // num_colors
    gradient_text = ""
    for i, char in enumerate(text):
        color_index = min(i // gradient_steps, num_colors - 1)
        gradient_text += f"{gradient_colors[color_index]}{char}"

    return f"{gradient_text}{RESET}"


banner_text = """

        S.       .S_SSSs     .S  sdSS_SSSSSSbs    sSSs_sSSs     .S S.    .S S.   
        SS.     .SS~SSSSS   .SS  YSSS~S%SSSSSP   d%%SP~YS%%b   .SS SS.  .SS SS.  
        S%S     S%S   SSSS  S%S       S%S       d%S'     `S%b  S%S S%S  S%S S%S  
        S%S     S%S    S%S  S%S       S%S       S%S       S%S  S%S S%S  S%S S%S  
        S&S     S%S SSSS%S  S&S       S&S       S&S       S&S  S%S S%S  S%S S%S  
        S&S     S&S  SSS%S  S&S       S&S       S&S       S&S   SS SS    SS SS   
        S&S     S&S    S&S  S&S       S&S       S&S       S&S    S_S      S_S    
        S&S     S&S    S&S  S&S       S&S       S&S       S&S   SS~SS    SS~SS   
        S*b     S*S    S&S  S*S       S*S       S*b       d*S  S*S S*S  S*S S*S  
        S*S.    S*S    S*S  S*S       S*S       S*S.     .S*S  S*S S*S  S*S S*S  
         SSSbs  S*S    S*S  S*S       S*S        SSSbs_sdSSS   S*S S*S  S*S S*S  
          YSSP  SSS    S*S  S*S       S*S         YSSP~YSSY    S*S S*S  S*S S*S  
                       SP   SP        SP                       SP       SP       
                       Y    Y         Y                        Y        Y        
                                                                         
"""


intro = """

          ⠀⠀⠀⠀⠀⠀⠀⠀⠴⣷⣶⣤⣀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣾⣶⣶⣶⣶⣶⣦⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⣄⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⣾⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠋⠉⠉⠉⠙⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠟⣿⣿⣿⣿⡀⠀⠙⠿⣿⣿⣿⣷⣦⣄⣠⣶⣿⣿⣿⡿⠟⠋⠁⣸⣿⣿⣿⡟⢿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⢀⣿⣿⣿⣿⡿⠋⠀⠸⣿⣿⣿⣷⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⢀⣿⣿⣿⣿⠃⠀⠙⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
          ⠀⠀⠀⠀⣼⣿⣿⣿⡟⠁⠀⠀⠀⣿⣿⣿⣿⡁⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⢀⣾⣿⣿⣿⡏⠀⠀⠀⠈⢿⣿⣿⣿⣿⡀⠀⠀⠀
          ⠀⠀⠀⢰⣿⣿⣿⡿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣧⣤⣾⣿⣿⣿⡿⠛⠉⠉⠻⣿⣿⣿⣿⣷⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⡇⠀⠀⠀
          ⠀⠀⠀⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣧⠀⠀⠀
          ⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⡋⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠈⣿⣿⣿⡆⠀⠀
          ⠀⠀⠠⣿⣿⣿⡇⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣶⣄⡀⠀⣿⣿⣿⡇⠀⠀
          ⠀⠀⠀⣿⣿⣿⣧⣴⣿⣿⣿⣿⣿⠿⠋⠘⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠙⠿⣿⣿⣿⣿⣿⣶⣿⣿⣿⡁⠀⠀
          ⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢻⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡗⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⡀⠀⠀
          ⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣶⣶⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣦⠀
          ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
          ⠀⠈⢹⠏⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣧⠀⠀⠀⠀⠀⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠉⠉⠉⣩⣿⣿⣿⠋⡏⢹⠀⠀
          ⠀⠀⠈⠀⠸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡆⠀⠀⠀⣼⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⡏⠀⣿⠀⠀⠀
          ⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣟⠀⠀⣸⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡟⠀⠀⠋⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡄⢠⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⢻⣿⣿⣿⣧⣿⣿⣿⣿⡟⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣷⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣁⣤⣤⣶⣾⣿⣿⣿⣿⣿⡿⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠻⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣿⢹⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             Laitoxx deanon tool! By: Asoru Telegram: @perehodasoru
                               Press to Enter
"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.045, enter=True)


def gmail_osint():
    def search_google_account(email_prefix):
        url = f"https://gmail-osint.activetk.jp/{email_prefix}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Failed to retrieve profile.")
            return None
    email_prefix = input(
        f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Enter the email prefix (e.g., for example@gmail.com, enter example): {Color.RESET}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Searching for Google profile...")
    profile_html = search_google_account(email_prefix)
    if profile_html:
        soup = BeautifulSoup(profile_html, 'html.parser')
        result_div = soup.find('div', style="margin:16px auto;text-align:center;display:block;border:1px solid #000;")
        if result_div:
            content = ''
            for element in result_div.descendants:
                if element.name == 'pre':
                    continue
                if element.string:
                    content += element.string.strip() + '\n'
            lines = content.split('\n')
            formatted_content = f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Google Account data\n\n"
            for line in lines:
                if 'Custom profile picture' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Custom profile picture:\n{lines[lines.index(line) + 1]}\n\n"
                elif 'Last profile edit' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Last profile edit:\n{line.split(': ')[1]}\n\n"
                elif 'Email' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Email:\n{lines[lines.index(line) + 1]}\n\n"
                elif 'Gaia ID' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Gaia ID:\n{line.split(': ')[1]}\n\n"
                elif 'User types' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} User types:\n{lines[lines.index(line) + 1]}\n\n"
                elif 'Profile page' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Google Maps Profile page:\n{lines[lines.index(line) + 1]}\n\n"
                elif 'No public Google Calendar' in line:
                    formatted_content += f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} No public Google Calendar.\n\n"
            print(f"{Color.DARK_RED}{formatted_content.strip()}{Color.RESET}")
        else:
            print(f"{Color.DARK_RED}{profile_html}{Color.RESET}")
    else:
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Failed to retrieve profile.")

def search_by_number():
    phone = input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Phone number: ")
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

    def validate_phone(phone):
        try:
            parsed_number = phonenumbers.parse(phone, "RU")
            return phonenumbers.is_valid_number(parsed_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            return False

    if not validate_phone(phone):
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Invalid number.")
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Try again, only without spaces and with '+'.")
        return

    try:
        infoPhone = urllib.request.urlopen(getInfo)
    except:
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} [!] - Information not found! - [!]")
        return

    infoPhone = json.load(infoPhone)

    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Mobile number: {phone}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Country: {infoPhone.get('country', {}).get('name')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Region: {infoPhone.get('region', {}).get('name')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Latitude: {infoPhone.get('capital', {}).get('latitude')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Longitude: {infoPhone.get('capital', {}).get('longitude')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Time zone: +{infoPhone.get('0', {}).get('time_zone')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} English city name: {infoPhone.get('0', {}).get('english')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} District: {infoPhone.get('0', {}).get('rajon')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Subdistrict: {infoPhone.get('0', {}).get('sub_rajon')}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Sound: {infoPhone.get('0', {}).get('sound')}")

    def search_vk_by_phone(phone):
        response = requests.get(f"https://find.vk.com/phone/{phone}")
        if response.status_code == 200:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} VK found!")
            return response
        else:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} VK not found")

    result = search_vk_by_phone(phone)
    if result is not None:
        print(result)
    else:
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} User with this phone number not found in VK.")

    url = f'https://www.avito.ru/rossiya/telefony?q={phone}'
    response = requests.head(url)
    if response.status_code == 200:
        print(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Avito found')
    else:
        print(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Avito not found')

    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[0{Color.DARK_RED}] https://www.google.com/maps/place/{infoPhone.get('capital', {}).get('latitude')},{infoPhone.get('capital', {}).get('longitude')} - Google maps")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[1{Color.DARK_RED}] TG: t.me/{phone}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[2{Color.DARK_RED}] https://api.whatsapp.com/send/?phone={phone}&text&type=phone_number&app_absent=0 - Whatsapp")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[3{Color.DARK_RED}] https://transitapp.com/redirect.html?url=viber://chat?number={phone} - VIBER")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[4{Color.DARK_RED}] https://www.phoneradar.ru/phone/{phone} - Rating")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[5{Color.DARK_RED}] https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink - OK account search")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[6{Color.DARK_RED}] https://www.phoneradar.ru/phone/{phone}")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[7{Color.DARK_RED}] https://twitter.com/account/begin_password_reset - Twitter account search")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[8{Color.DARK_RED}] https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Facebook account search")
    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}[9{Color.DARK_RED}] skype:{phone}?call - Call number with Skype")

    def google_search_phone(phone):
        query = f"https://www.google.com/search?q={phone}"
        response = requests.get(query)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a')
            links = []
            for result in search_results:
                href = result.get('href')
                if href.startswith('/url?q='):
                    link = href.replace('/url?q=', '').split('&')[0]
                    links.append(link)
            if len(links) > 0:
                print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Links found:")
                for link in links:
                    print(link)
            else:
                print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Links not found")
        else:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Error during request")

    google_search_phone(phone)


def temp_mail():
    def create_temp_mail():
        local_part = input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Enter name: {Color.DARK_RED}")
        domain = "rteet.com"
        email = f"{local_part}@{domain}"
        return email

    def get_mailbox_messages(login, domain):
        response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Failed to retrieve messages.")
            return []

    def get_message_details(login, domain, message_id):
        response = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Failed to retrieve message details.")
            return None

    def extract_text_from_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()

    def save_message_to_file(filename, sender, date, subject, body):
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}From: {sender}\n')
            file.write(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Date: {date}\n')
            file.write(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Subject: {subject}\n')
            file.write(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Message: {body}\n\n')

    def adjust_time(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        adjusted_time = date_obj + timedelta(hours=3)
        return adjusted_time.strftime("%Y-%m-%d %H:%M:%S")

    email = create_temp_mail()
    if email:
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Temporary email used: {Color.DARK_RED}{email}{Color.RESET}")

        login, domain = email.split('@')
        processed_messages = set()

        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Checking for new messages...")
        while True:
            messages = get_mailbox_messages(login, domain)
            if messages:
                for message in messages:
                    if message['id'] not in processed_messages:
                        message_details = get_message_details(login, domain, message['id'])
                        if message_details:
                            sender = message_details["from"]
                            date = adjust_time(message_details["date"])
                            subject = message_details["subject"]
                            message_body = extract_text_from_html(message_details["body"])
                            save_message_to_file('emails.txt', sender, date, subject, message_body)

                            print()
                            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} From: {Color.DARK_RED}{sender}{Color.RESET}")
                            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Date: {Color.DARK_RED}{date}{Color.RESET}")
                            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Subject: {Color.DARK_RED}{subject}{Color.RESET}")
                            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Message: {Color.DARK_RED}{message_body}\n{Color.RESET}")

                        processed_messages.add(message['id'])
            time.sleep(5)

def check_email_address(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Email address is valid{Color.RESET}"
    else:
        return f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Invalid email address{Color.RESET}"

def get_ip():
    ip = input(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Enter IP: ')

    try:
        ip = socket.gethostbyname(ip)

        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()

        if infoList.get("success"):
            print(f'''{Color.DARK_RED}

      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}IP Address:   {infoList["ip"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Success:      {infoList["success"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Type:         {infoList["type"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Continent:    {infoList["continent"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Country:      {infoList["country"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Region:       {infoList["region"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}City:         {infoList["city"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Postal Code:  {infoList["postal"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Capital:      {infoList["capital"]}

''')
        else:
            print(f'''{Color.DARK_RED}

      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}IP:           {infoList["ip"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Success:      {infoList["success"]}
      {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Message:      {infoList["message"]}

''')
    except Exception as e:
        print(f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}An error occurred: {e}')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(4):
        print()

    print(f"""{gradient_text(banner_text)}                      
            
                                        {Color.DARK_GRAY}By: {Color.DARK_RED}Asoru
                                        
                                 {Color.DARK_GRAY}[{Color.DARK_RED}1{Color.DARK_GRAY}] {Color.DARK_RED}Check Phone Number              
                                 {Color.DARK_GRAY}[{Color.DARK_RED}2{Color.DARK_GRAY}] {Color.DARK_RED}Check IP                                    
                                 {Color.DARK_GRAY}[{Color.DARK_RED}3{Color.DARK_GRAY}] {Color.DARK_RED}Validate Email                              
                                 {Color.DARK_GRAY}[{Color.DARK_RED}4{Color.DARK_GRAY}] {Color.DARK_RED}About the Software                          
                                 {Color.DARK_GRAY}[{Color.DARK_RED}5{Color.DARK_GRAY}] {Color.DARK_RED}Support the Author                         
                                 {Color.DARK_GRAY}[{Color.DARK_RED}6{Color.DARK_GRAY}] {Color.DARK_RED}Check Website                     
                                 {Color.DARK_GRAY}[{Color.DARK_RED}8{Color.DARK_GRAY}] {Color.DARK_RED}Strange Text                                
                                 {Color.DARK_GRAY}[{Color.DARK_RED}9{Color.DARK_GRAY}] {Color.DARK_RED}Password Generator                          
                                 {Color.DARK_GRAY}[{Color.DARK_RED}10{Color.DARK_GRAY}] {Color.DARK_RED}Port Scanner
                                 {Color.DARK_GRAY}[{Color.DARK_RED}11{Color.DARK_GRAY}] {Color.DARK_RED}Temp Mail
                                 {Color.DARK_GRAY}[{Color.DARK_RED}12{Color.DARK_GRAY}] {Color.DARK_RED}Gmail Osint                               
                                 {Color.DARK_GRAY}[{Color.DARK_RED}66{Color.DARK_GRAY}] {Color.DARK_RED}Exit                                       

    """)

    prompt_text = f'{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Select an option'
    final_prompt = f"{prompt_text}{Color.DARK_RED} > {Color.DARK_RED}"
    select = input(final_prompt)

    if select == '66':
        subprocess.run(['python', '/storage/emulated/0/honkai/main.py'])
    elif select == '1':
        search_by_number()
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")
    elif select == '3':
        email = input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Enter email address: ")
        print(check_email_address(email))
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")
    elif select == '2':
        get_ip()
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")
    elif select == '4':
        print(
            f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}The author is not responsible for users. The software was created for educational purposes only. All sources are public and the author has no relation to them.")
        print("Thank you for choosing us!")
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")
    elif select == '5':
        print(f"""{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}I would be grateful if you could donate for some dumplings <3
        @send (telegram bot):t.me/send?start=IV1xARFXeILV
        """)
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")
    elif select == '6':
        domain = input(f"{Color.DARK_RED}Enter website: ")

        def get_website_info(domain):
            domain_info = whois.whois(domain)
            print_string = f"""
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Domain: {domain_info.domain_name}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Registered: {domain_info.creation_date}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Expires: {domain_info.expiration_date}  
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Owner: {domain_info.registrant_name}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Organization: {domain_info.registrant_organization}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Address: {domain_info.registrant_address}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} City: {domain_info.registrant_city}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} State: {domain_info.registrant_state}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Postal Code: {domain_info.registrant_postal_code}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Country: {domain_info.registrant_country}
    {Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} IP Address: {domain_info.name_servers}
            """

        get_website_info(domain)
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")

    elif select == '8':
        def transform_text(input_text):
            translit_dict = {
                "а": "@", "б": "Б", "в": "B", "г": "г", "д": "д", "е": "е", "ё": "ё", "ж": "ж", "з": "3",
                "и": "u", "й": "й", "к": "K", "л": "л", "м": "M", "н": "H", "о": "0", "п": "п", "р": "P",
                "с": "c", "т": "T", "у": "y", "ф": "ф", "х": "X", "ц": "ц", "ч": "4", "ш": "ш", "щ": "щ",
                "ъ": "ъ", "ы": "ы", "ь": "ь", "э": "э", "ю": "ю", "я": "я", "А": "A", "Б": "6", "В": "V",
                "Г": "r", "Д": "D", "Е": "E", "Ё": "Ё", "Ж": "Ж", "З": "2", "И": "I", "Й": "Й", "К": "K",
                "Л": "Л", "М": "M", "Н": "H", "О": "O", "П": "П", "Р": "P",
            }
            transformed_text = []
            for char in input_text:
                if char in translit_dict:
                    transformed_text.append(translit_dict[char])
                else:
                    transformed_text.append(char)
            return "".join(transformed_text)


        input_text = input(f"{Color.DARK_RED}Enter text: {Color.DARK_RED}")
        transformed_text = transform_text(input_text)
        print(
            f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Result: {transformed_text}{Color.RESET}")
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED} Press Enter.....{Color.RESET}")

    import string
    import random

    if select == '9':
        def get_characters(complexity):
            characters = string.ascii_letters + string.digits
            if complexity == "medium":
                characters += "!@#$%^&*()qwertyuiop[]{}asdfghjkl;'zxcvbnm<>?/|1234567890-_=+"
            elif complexity == "high":
                characters += string.punctuation
            return characters

        def generate_password(length, complexity):
            characters = get_characters(complexity)
            password = "".join(random.choice(characters) for i in range(length))
            return password

        password_length = int(input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Enter password length -> "))
        complexity = input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Choose complexity (low, medium, high): ")
        print()
        complex_password = generate_password(password_length, complexity)
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Password: {complex_password}")
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")

    if select == '10':
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Choose mode: ")
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}1 - Check commonly used ports")
        print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}2 - Check specific port")
        mode = input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Your choice: ")
        if mode == '1':
            print()
            ports = [
                20, 26, 28, 29, 55, 53, 80, 110, 443, 8080, 1111, 1388, 2222, 1020, 4040, 6035
            ]
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(("127.0.0.1", port))
                if result == 0:
                    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Port {port} is open")
                else:
                    print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Port {port} is closed")
                sock.close()
                print()
        elif mode == '2':
            port = input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Enter port number: ")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("127.0.0.1", int(port)))
            print()
            if result == 0:
                print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Port {port} is open")
            else:
                print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Port {port} is closed")
            sock.close()
            print()
        else:
            print(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Unknown mode")
            print()
            input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")
    elif select == '11':
        temp_mail()
    elif select == '12':
        gmail_osint()
        input(f"{Color.DARK_GRAY}[{Color.DARK_RED}⛧{Color.DARK_GRAY}]{Color.DARK_RED}Press Enter.....")

