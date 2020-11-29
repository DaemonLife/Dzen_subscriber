from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search
from selenium.webdriver.common.by import By # method of search

from time import sleep

def first_login(finder):
    
    path = "//*[contains(text(), 'Войти')]"
    el = finder.element_by_xpath(path)
    el.click()

def send_login_password(finder, login, password, link, count):
    driver = finder.driver
    el = finder.element_by_name('login', 2)
    try:
        el.send_keys(login)
        path = "//button[@type='submit']"
        el = finder.element_by_xpath(path)
        el.click()
        # Отправка пароля
        sleep(0.25)
        el = finder.element_by_name('passwd')
        el.send_keys(password)
    except:
        print('Перенаправление 1')
        driver.get(link)
        click_login_button(finder, login, password, link, count)
        select_other_acc(finder, login, password, link, count)
        send_login_password(finder, login, password, link, count)

        return 0

def click_subscribe_button(finder, login, password, link, count, flows):
    driver = finder.driver
    # path = "//span[contains(text(), 'Подписаться')]"
    path = '//div[3]/div/div/div/div/button' # subscribe button in div[3]
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element = driver.find_element_by_xpath(path)
    except: # если не найдена кнопка, то возможно просит телефон. Пробуем отказаться.
        el = '//form/div[3]/button' 
        el = finder.element_by_xpath(el)
        try:
            el.click()
            # пробуем снова подписаться. 
            try:
                element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, path))
                )
            except: 
                print('Не удалось обнаружить кнопку подписки')
                return 0
        except:
            pass
    try:
        element = driver.find_element_by_xpath(path)
        element.click()
        print(f'Подписался')
    except:
        print('Не удалось нажать кнопку подписки')
        return 0

def open_menu_user(finder, login, password, link, count):
    driver = finder.driver
    path = '//nav/div[3]/div[3]/button'
    el = finder.element_by_xpath(path)
    try:
        el.click()
    except:
        # print('Перенаправление 3')
        driver.get(link)
        open_menu_user(finder, login, password, link, count)

        return 0

def click_exit_button(finder, login, password, link, count):
    driver = finder.driver
    path = '//div/div/div[3]/a'
    el = finder.element_by_xpath(path)
    try:
        el.click()
    except:
        # print('Перенаправление 4')
        driver.get(link)
        open_menu_user(finder, login, password, link, count)
        click_exit_button(finder, login, password, link, count)

        return 0

def click_login_button(finder, login, password, link, count):
    driver = finder.driver
    path = "//*[contains(text(), 'Войти')]"
    el = finder.element_by_xpath(path)
    try:
        el.click()
    except:
        # print('Перенаправление 5')
        driver.get(link)
        click_login_button(finder, login, password, link, count)

        return 0

def select_other_acc(finder, login, password, link, count):
    driver = finder.driver
    if count < 2:
        path = '//form/div[1]/a'
        el = finder.element_by_xpath(path)
        try:
            el.click()   
        except:
            pass
    path = '//a/span/span'
    try:
        for i in range(1):
            try:
                element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, path))
                )
                element = driver.find_element_by_xpath(path)
                element = element.find_element_by_xpath('../..')
                element.click()
            except:
                pass

    except:
        # print('Перенаправление 6')
        driver.get(link)
        click_login_button(finder, login, password, link, count)
        select_other_acc(finder, login, password, link, count)

        return 0
    
