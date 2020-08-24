from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import platform # определение платформы
import random
from datetime import timedelta, datetime

from urllib.request import urlopen
import pickle # печеньки

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def my_system():
    my_sys = (platform.platform())[:5]
    if my_sys == "Linux":
        return "Linux"
    elif my_sys == "Windo":
        return "Windows"
    elif my_sys == "macOS":
        return "MacOS"

if (my_system() == "Linux") or (my_system() == "MacOS"):
    BASE_DIR += "/"
elif my_system() == "Windo":
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

    opts.add_argument("--headless") 
    driver = webdriver.Chrome(chrome_options=opts, executable_path=r'' + BASE_DIR + driver_path)

    return driver # возвращаем объект

def authorization(driver, username, password):
    #ВХОД В АККАУНТ
    driver.get('https://www.facebook.com/login')
    sleep(3)

def open_sign():

    my_sys = my_system()
    if my_sys == "Windows":
        file_path = 'files\\accounts.txt'
    elif my_sys == "Linux":
        file_path = 'files/accounts.txt'
    elif my_sys == "MacOS":
        file_path = 'files/accounts.txt'

    f = open(BASE_DIR + file_path, 'r')
    acc_list = []
    for line in f:
        acc_list.append(line)
    f.close()
    return acc_list
