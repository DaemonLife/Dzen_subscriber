import threading, random
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search

from selenium.webdriver.common.by import By # method of search

from libraries import *

def subscribing(i, link, account):
    num = 'Proc.' + str(i) + ':'
    x = account.split(':')
    login = x[0]
    password = x[1]

    driver = driver_start()
    driver.get(link)

    # ---------------- Login ---------------- #

    # --------- step 1 ---------- #

    path = "//*[contains(text(), 'Войти')]"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element = driver.find_element_by_xpath(path)
    except:
        print(num, '<Войти> не найдено')

    try:
        element.click()
    except:
        print(num, 'Ошибка нажатия <Войти>')

    # --------- step 2 ---------- #

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login'))
        )
        element = driver.find_element_by_name('login')
    except:
        print(num, '<login> не найдено')

    try:
        element.send_keys(login)
    except:
        print(num, 'Ошибка ввода в <login>')

    # --------- step 3 ---------- #

    path = "//button[@type='submit']"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element = driver.find_element_by_xpath(path)
    except:
        print(num, '<submit 1> не найдено')

    try:
        element.click()
    except:
        print(num, 'Ошибка нажатия <submit 1>')

    # --------- step 4 ---------- #

    # path = "//input[@type='password']"
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, path))
    #     )
    #     element = driver.find_element_by_xpath(path)
    # except:
    #     print('<password> не найдено')

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'passwd'))
        )
        element = driver.find_element_by_name('passwd')
    except:
        print(num, '<password> не найдено')

    try:
        element.send_keys(password)
    except:
        print(num, 'Ошибка ввода в <password>')

    # --------- step 5 ---------- #
    # sleep(0.5)
    # path = "//button[@type='submit']"
    # try:
    #     element = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located((By.XPATH, path))
    #     )
    #     element = driver.find_element_by_xpath(path)
    # except:
    #     print(num, '<submit 2> не найдено')

    # try:
    #     element.click()
    # except:
    #     print(num, 'Ошибка нажатия <submit 2>')

    # -------------- End Login -------------- #

    # ----------- Click on button ----------- #

    path = '//div[3]/div/div/div/div/button'
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element = driver.find_element_by_xpath(path)
    except:
        print(num, '<button subscribe> не найдено')

    try:
        element.click()
        print(num, 'successful comlited!')
    except:
        print(num, 'Ошибка нажатия <button subscribe>')
        print(num, 'Error comlited!')

    sleep(6)
    driver.quit()
    print(num, 'end')

accounts = open_sign()

# link = 'https://zen.yandex.ru/gaming_news'
link = 'https://zen.yandex.ru/fitness13'

for i in range(5):
    account = accounts[i]
    threading.Thread(target=subscribing, args=[i, link, account]).start()
    print('Proc.' + str(i), 'start')