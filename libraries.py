from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import platform # определение платформы
import threading, random
from datetime import timedelta, datetime

from urllib.request import urlopen
import pickle # печеньки

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def licence(d, m, y):
   res = urlopen('http://just-the-time.appspot.com/')
   result = res.read().strip()
   result_str = result.decode('utf-8')
   x = result_str.split(" ")
   today_date = x[0].split("-")
   now = datetime(int(today_date[0]), int(today_date[1]), int(today_date[2]))
   end_time = datetime(y, m, d)
#    print(end_time)
#    print(now)
   if (now >= end_time):
       if (os.path.exists('key5543y7.txt') == 1):
           print('Key is here')
           return 1
       print('Заплати - и получи ключ!')
       pause = input(' . . . ')
       return 0
   else:
       return 1

def my_system():
    my_sys = (platform.platform())[:5]
    if my_sys == "Linux":
        return "Linux"
    elif my_sys == "Windo":
        return "Windows"
    

if (my_system() == "Linux") or (my_system() == "MacOS"):
    BASE_DIR += "/"
elif my_system() == "Windows":
    BASE_DIR += "\\"
else:
    print('Ошибка определения вашей системы')

def driver_start():
    my_sys = my_system()
    if my_sys == "Windows":
        driver_path = 'driver\\Windows\\chromedriver.exe'
    elif my_sys == "Linux":
        driver_path = 'driver/Linux/chromedriver'
    elif my_sys == "MacOS":
        driver_path = 'driver/MacOS/chromedriver'

    opts = Options()

    # mobile_emulation = { "deviceName": "iPhone X" } # type your device from list
    # opts.add_experimental_option("mobileEmulation", mobile_emulation)

    # opts.add_argument("--headless") 
    driver = webdriver.Chrome(chrome_options=opts, executable_path=r'driver\\Windows\\driver.exe')

    return driver # возвращаем объект

def open_sign():

    my_sys = my_system()
    if my_sys == "Windows":
        file_path = 'files\\accounts.txt' # система курильщика
    elif my_sys == "Linux":
        file_path = 'files/accounts.txt'  # нормальная система
    elif my_sys == "MacOS":
        file_path = 'files/accounts.txt'  # нормальная система

    f = open('files\\accounts.txt', 'r')
    acc_list = []
    for line in f:
        acc_list.append(line)
    f.close()
    return acc_list

def open_links():

    my_sys = my_system()
    if my_sys == "Windows":
        file_path = 'files\\accounts.txt' # система курильщика
    elif my_sys == "Linux":
        file_path = 'files/accounts.txt'  # нормальная система
    elif my_sys == "MacOS":
        file_path = 'files/accounts.txt'  # нормальная система

    f = open('files\\links.txt', 'r')
    links_list = []
    for line in f:
        links_list.append(line)
    f.close()
    return links_list
