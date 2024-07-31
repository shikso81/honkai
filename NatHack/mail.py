#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
import os
import pandas as pd
import sqlite3

COLOR_CODE = {
    "RESET": "\033[0m",
    "RED": "\033[31m",
}

def search_email_in_folder(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f'{COLOR_CODE["RED"]}Ошибка: "{folder_path}" не является папкой или не существует.{COLOR_CODE["RESET"]}')
        return
    search_value = input(f'{COLOR_CODE["RED"]}Введите email для поиска: {COLOR_CODE["RESET"]}')
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                for line in lines:
                    if search_value in line:
                        print(
                            f'{COLOR_CODE["RED"]}Найден email {search_value} в файле: {file_path}{COLOR_CODE["RESET"]}')
                        print(f'{COLOR_CODE["RED"]}Информация о email:{COLOR_CODE["RESET"]}')
                        print(line)
                        print('\n')
    input(f'{COLOR_CODE["RED"]}Нажмите Enter......{COLOR_CODE["RESET"]}')
    return
def read_sql_file(file_path):
    with open(file_path, 'r') as sql_file:
        sql_query = sql_file.read()
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(sql_query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=columns)
    conn.close()
    return df
folder_path = 'database'
search_email_in_folder(folder_path)
import main
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru