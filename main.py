import threading, random
from time import sleep

from libraries import *

def subscribing(i, link):
    driver = driver_start()
    driver.get(link)
    driver.quit()
    print('Процесс', i, 'остановлен')

link = 'https://www.google.com/'

for i in range(2):
    threading.Thread(target=subscribing, args=[i+1, link]).start()
    print('Процесс', i+1, 'запущен')