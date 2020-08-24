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


def subscribing(i, link, arr):

    driver = driver_start()
    finder = Finder(driver)
    driver.get(link)
    trye_url = driver.current_url
    count = 0
    for acc in arr:
        print(f'Proc.{i} подписка...')
        x = acc.split(':')
        login = x[0]
        password = x[1]

        # ---------------- Login ---------------- #

        # --------- Первый раз Кнопка Войти ---------- #

        if count == 0:
            path = "//*[contains(text(), 'Войти')]"
            el = finder.element_by_xpath(path)
            el.click()

        # --------- Отправка логина ---------- #

        el = finder.element_by_name('login')
        el.send_keys(login)


        path = "//button[@type='submit']"
        el = finder.element_by_xpath(path)
        el.click()

        # --------- Отправка пароля ---------- #

        el = finder.element_by_name('passwd')
        el.send_keys(password)

        # --------- Если попросит телефон ---------- # random otional
        if driver.current_url != trye_url:
            path = '//button'
            els = finder.elements_by_xpath(path, 1)
            try:
                element = els[1]
                element.click()
            except:
                pass

        # -------------- End Login -------------- #

        # Подписаться

        path = "//span[contains(text(), 'Подписаться')]"
        try:
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            element = driver.find_element_by_xpath(path)
        except:
            pass
        try:
            element = element.find_element_by_xpath('..')
            element.click()
        except:
            pass


        # ------------------ Exit ------------------ #

        # Открыть меню юзера
        
        path = '//nav/div[3]/div[3]/button'
        el = finder.element_by_xpath(path)
        try:
            el.click()
        except:
            print('Err 1')

        # Нажать Выйти
        
        path = '//div/div/div[3]/a'
        el = finder.element_by_xpath(path)
        try:
            el.click()
        except:
            print('Err 2')
        
        # Нажать Войти

        path = "//*[contains(text(), 'Войти')]"
        el = finder.element_by_xpath(path)
        try:
            el.click()
        except:
            print('Err 3')

        # Выбрать другой акк
        if count < 2:
            path = '//form/div[1]/a'
            el = finder.element_by_xpath(path)
            try:
                el.click()   
            except:
                print('Err 4')

        path = '//a/span[2]'
        try:
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            element = driver.find_element_by_xpath(path)
        except:
            pass
        try:
            element = element.find_element_by_xpath('..')
            element.click()
        except:
            pass

        count += 1
        print(f'Proc.{i} подписка завершена, число подписок потока {i}: {count}')


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

    # opts.add_argument("--headless") 
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
