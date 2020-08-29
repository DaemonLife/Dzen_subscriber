from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search
from selenium.webdriver.common.by import By # method of search

from libraries import sleep, driver_start, open_sign, random, threading, licence

from finder import Finder 

def subscribing(i, link, arr):
    driver = driver_start()
    finder = Finder(driver)
    driver.get(link)
    count = 0
    for acc in arr:
        print(f'Proc.{i} подписка...')
        x = acc.split(':')
        login = x[0]
        password = x[1]

        # ---------------- Login ---------------- #

        # Первый раз Кнопка Войти 

        if count == 0:
            path = "//*[contains(text(), 'Войти')]"
            el = finder.element_by_xpath(path)
            el.click()

        # Отправка логина 

        el = finder.element_by_name('login', 2)
        try:
            el.send_keys(login)
        except: # хз почему эта ошибка возникает, костыль
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
                el = finder.element_by_name('login', 2)
                el.send_keys(login)
            except:
                pass

        path = "//button[@type='submit']"
        el = finder.element_by_xpath(path)
        el.click()

        # Отправка пароля
        sleep(0.25)
        el = finder.element_by_name('passwd')
        el.send_keys(password)

        # -------------- End Login -------------- #

        # Подписаться
        path = "//span[contains(text(), 'Подписаться')]"
        try:
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            element = driver.find_element_by_xpath(path)
        except: # если не найдена кнопка, то возможно просит телефон. Пробуем отказаться.
            path = '//form/div[3]/button' 
            el = finder.element_by_xpath(path)
            try:
                el.click()
                # пробуем снова подписаться. 
                path = "//span[contains(text(), 'Подписаться')]"
                try:
                    element = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, path))
                    )
                    element = driver.find_element_by_xpath(path)
                except: 
                    pass
            except: # видимо вообще все зависло, попробуем обновить страницу
                driver.get(link)
                print('Err 0')
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
        except: # видимо вообще все зависло, попробуем обновить страницу
            driver.get(link)
            print('Err 1')

        # Нажать Выйти
        
        path = '//div/div/div[3]/a'
        el = finder.element_by_xpath(path)
        try:
            el.click()
        except: # видимо вообще все зависло, попробуем обновить страницу
            driver.get(link)
            print('Err 2')
        
        # Нажать Войти

        path = "//*[contains(text(), 'Войти')]"
        el = finder.element_by_xpath(path)
        try:
            el.click()
        except: # видимо вообще все зависло, попробуем обновить страницу
            driver.get(link)
            print('Err 3')

        # Выбрать другой акк
        if count < 1:
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


li = licence(26, 8, 2020)

if li == 1:

    accounts = open_sign() 

    print('Введите необходимую ссылку. Пример: https://zen.yandex.ru/fitness13')
    link = input('Ввод ссылки: ')
    accs = int(input('Введите нужное число подписок: '))
    flows_max = int(input('Введите число потоков: '))

    i = 0
    new_accounts = []
    # создание массива нужного количества аккаутов из всех базы данных аккаунтов 
    # (на основе того сколько подписок нужно осуществить)
    for line in accounts:
        new_accounts.append(line)
        i += 1
        if i > accs:
            break

    del accounts, accs # удаление уже ненежных переменны

    # индексы для разделения общего массива аккаунтов
    first_index = 0
    second_index = 0
    for flows in range(flows_max): # создание потоков
        if second_index == 0:
            second_index = int(len(new_accounts)/flows_max) # разделение массива на равные части для каждого потока
        else:
            first_index = second_index
            second_index += second_index
            # коррекция погрешности при разделении массива
            if (flows == (flows_max-1)) and (second_index != len(new_accounts)):
                second_index = len(new_accounts) 
        arr = new_accounts[first_index:second_index] # создание временного массива для передачи в поток
        try:
            threading.Thread(target=subscribing, args=[flows, link, arr]).start()
            print(flows, 'поток запущен')
        except:
            print('err')