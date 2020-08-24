from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search
from selenium.webdriver.common.by import By # method of search

from libraries import sleep, driver_start, open_sign, random, threading, licence

from finder import Finder 

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

        # Первый раз Кнопка Войти 

        if count == 0:
            path = "//*[contains(text(), 'Войти')]"
            el = finder.element_by_xpath(path)
            el.click()

        # Отправка логина 

        el = finder.element_by_name('login')
        el.send_keys(login)


        path = "//button[@type='submit']"
        el = finder.element_by_xpath(path)
        el.click()

        # Отправка пароля

        el = finder.element_by_name('passwd')
        el.send_keys(password)

        # Если попросит телефон - random otional
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


li = licence(22, 8, 2020)

if li == 1:


    accounts = open_sign()

    print('Введите необходимую ссылку. Пример: https://zen.yandex.ru/fitness13')
    link = 'https://zen.yandex.ru/fitness13'
    link = input('Ввод ссылки:')

    accs = int(input('Введите нужное число подписок: '))
    flows_max = int(input('Введите число потоков: '))

    i = 0
    new_accounts = []
    for line in accounts:
        new_accounts.append(line)
        i += 1
        if i > accs:
            break

    del accounts, accs

    first_index = 0
    second_index = 0
    for flows in range(flows_max):
        if second_index == 0:
            second_index = int(len(new_accounts)/flows_max)
        else:
            first_index = second_index
            second_index += second_index
            while second_index > len(new_accounts)+1:
                second_index -= 1
        arr = new_accounts[first_index:second_index]
        try:
            threading.Thread(target=subscribing, args=[flows, link, arr]).start()
            print(flows, 'поток запущен')
        except:
            print('err')