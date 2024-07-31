#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
import socket
import requests

COLOR_CODE = { 
    "RED": "\033[31m",
}

def get_ip():
    ip = input(f'{COLOR_CODE["RED"]}[@]Введите айпи: ')

    try:
        ip = socket.gethostbyname(ip)
        
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()
        
        if infoList.get("success"):
            print(f'''{COLOR_CODE["RED"]}

      Айпи адресс:   {infoList["ip"]}
      Успех:         {infoList["success"]}
      Тип:           {infoList["type"]}
      Континент:     {infoList["continent"]}
      Страна:        {infoList["country"]}
      Регион:        {infoList["region"]}
      Город:         {infoList["city"]}
      Почтовый код:  {infoList["postal"]}
      Столица:       {infoList["capital"]}
                     
''')
        else:
            print(f'''{COLOR_CODE["RED"]}

      IP:           {infoList["ip"]}
      Success:      {infoList["success"]}
      Message:      {infoList["message"]}
                     
''')
    except Exception as e:
        print(f'{COLOR_CODE["RED"]}Произошла ошибка: {e}')
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru