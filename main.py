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

    # print('Поток', i, 'старт')
    sleep(random.randint(5,15))
    # print('Поток', i, 'конец')
    driver.quit()
    return 0

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

    # --------- step 5 ---------- # it's auto!
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

    # --------- step 6 ---------- # random otional
    path = '//button'
    button_is = 0
    try:
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, path))
        )
        elements = driver.find_elements_by_xpath(path)
        button_is = 1
    except:
        pass

    if button_is == 1:
        print(num, 'Отклонение просьбы добавить телефон')
        try:
            element = elements[1]
            element.click()
        except:
            print(num, 'Ошибка нажатия <Не сейчас>')  

    # -------------- End Login -------------- #
    # ----------- Click on button ----------- #


    # path = '//div[3]/div/div/div/div/button'
    path = "//span[contains(text(), 'Подписаться')]"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element = driver.find_element_by_xpath(path)
    except:
        print(num, '<Подписаться/span> не найдено')

    try:
        element = element.find_element_by_xpath('..')
        element.click()
        print(num, 'successful comlited!')
    except:
        print(num, 'Ошибка нажатия <Подписаться>')
        print(num, 'Error comlited!')

    # --------- End Click on button --------- #

    sleep(60)
    driver.quit()
    print(num, 'end')

accounts = open_sign()

# link = 'https://zen.yandex.ru/fitness13'
print('Введите необходимую ссылку. Пример: https://zen.yandex.ru/fitness13')
link = input('Ввод ссылки:')
subscribe_count = int(input('Введите нужное число подписок: '))
flows_max = int(input('Введите число потоков: '))

threads = []
count = 0
flows = 0
i = 0
b = 0
base_threading_active = threading.activeCount()
while True:
    while threading.activeCount() - base_threading_active < flows_max:
        try:
            x = threading.Thread(target=subscribing, args=[flows, link, accounts[i]])
        except:
            print(f'Выход за предел количества аккаунтов ({i+1}). Работа завершена.')
            b = 1
            break
        threads.append(x)
        x.start()

        i += 1
        if i >= subscribe_count:
            b = 1
            break
    print('Число потоков:', threading.activeCount()-base_threading_active, 'Число вып. действий:', i, end='\r')

    if b == 1:
        break

while base_threading_active != threading.activeCount():
    sleep(1)

print(f'\n\nВсе операции завершены!')
pause = input('Введите <Enter> для выхода...')