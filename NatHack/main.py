#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
import os
from pystyle import Colorate, Colors
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(4):
        print()

    from banner import banner
    print(Colorate.Horizontal(Colors.cyan_to_blue, banner.strip()))

    COLOR_CODE = {
        "RESET": "\033[0m",
        "UNDERLINE": "\033[04m",
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

    prompt_text = f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["RED"]} Выберите опцию'
    final_prompt = f"{prompt_text}{COLOR_CODE['RED']} > {COLOR_CODE['RESET']}"

    select = input(final_prompt)

    if select == '1':
        from search import search_phone_number_in_folder
        database_folder = 'database'
        search_value = input(
            f'{COLOR_CODE["RED"]}Введите номер телефона: ')
        database_files = [os.path.join(database_folder, filename) for filename in os.listdir(database_folder)]
        for database_file in database_files:
            search_phone_number_in_folder(database_file, search_value)
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '3':
        from mail import search_email_in_folder
        database_folder = 'database'
        search_value = input(f'{COLOR_CODE["RED"]}Введите почту: ')
        database_files = [os.path.join(database_folder, filename) for filename in os.listdir(database_folder)]
        for database_file in database_files:
            search_email_in_folder(database_file)
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '2':
        from get_ip import get_ip
        get_ip()
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '4':
        from ddos import dos
        dos()
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '5':
        import proxy
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '6':
        from tokenbot import token_bot
        token_bot()
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '7':
        from vk import vkinfo
        apivk = input(f'{COLOR_CODE["RED"]} Вк токен : ')
        user_id = input(f'{COLOR_CODE["RED"]} Введите ID или ссылку вк профиля: ')
        if user_id.startswith('https://vk.com/'):
            user_id = user_id[len('https://vk.com/'):]
        vkinfo(user_id, apivk)
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '8':
        import fishtg
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")

    elif select == '1488':
        print(f"""{COLOR_CODE["RED"]}Слава Эщкерии! 
                 Слава Медным быкам! 
                 Слава Чёрным Дельфинам! 
                 Миньоны и Хрюшки 
                 Мы весь мир поднимем на ушки! 
                 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐""")
        input("Нажмите Enter, чтобы продолжить(UPDATE BY @peregodasoru)...")


    elif select == '99':
        exit()

    else:
        print(f'{COLOR_CODE["RED"]}Неверный выбор, попробуйте снова!(UPDATE BY @peregodasoru)')
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru