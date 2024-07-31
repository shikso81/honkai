#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
import os
import requests
from colorama import init, Fore, Style
init()
def get_proxy():
    proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
    try:
        response = requests.get(proxy_api_url)
        if response.status_code == 200:
            proxy_list = response.text.strip().split("\r\n")
            return proxy_list
        else:
            print(
                f"{Fore.RED}Failed to fetch proxy list. Status code: {response.status_code}"
            )
    except Exception as e:
        print(
            f"{Fore.RED}Error fetching proxy list: {e}"
        )
    return None
proxies = get_proxy()
if proxies:
    print(f"{Style.BRIGHT}{Fore.GREEN}Proxy list:")
    for proxy in proxies:
        print(f"{Style.BRIGHT}{Fore.GREEN}{proxy}")
else:
    print(
        f"{Fore.RED}No proxy list available."
    )
input(f"{Style.BRIGHT}{Fore.GREEN}Press Enter...")
os.system("python main.py")
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru