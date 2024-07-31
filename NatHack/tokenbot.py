import subprocess
import requests
from colorama import init, Fore

init()

def get_token_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    if response.status_code == 200:
        token_info = response.json()
        return token_info
    else:
        print(Fore.RED + "Error: Unable to fetch token info")
        return None

def display_token_info(token_info):
    if token_info:
        print(Fore.GREEN + f"""
        Token: {token_info['result']['id']} 
        id: {token_info['result']['id']} 
        is_bot: {token_info['result']['is_bot']}
        first_name: {token_info['result']['first_name']}
        username: {token_info['result']['username']}
        can_join_groups: {token_info['result']['can_join_groups']}
        supports_inline_queries: {token_info['result']['supports_inline_queries']}
        """)
    else:
        print(Fore.RED + "No token info available.")

def press_enter_to_continue():
    input(Fore.YELLOW + "Press Enter...")
    subprocess.run(["python", "main.py"])

def token_bot():
    token = input(Fore.BLUE + "Enter your bot token: ")
    token_info = get_token_info(token)
    display_token_info(token_info)
    press_enter_to_continue()

if __name__ == "__main__":
    token_bot()
