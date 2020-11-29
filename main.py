from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search
from selenium.webdriver.common.by import By # method of search

from libraries import sleep, driver_start, open_sign, open_links, random, threading, licence

from finder import Finder 

from small_functions import *

def subscribing(i, link, arr):
    try:
        driver = driver_start()
    except:
        print('Ошибка драйвера\n')
        pause = input('Введите <Enter> для выхода из потока . . .')
        return 0
    finder = Finder(driver)
    driver.get(link)
    count = 0
    sleep(i*2.5)
    for acc in arr:
        print(f'Proc.{i} подписка...')
        x = acc.split(':')
        login = x[0]
        password = x[1]

        # Первый раз Кнопка Войти 
        if count == 0:
            first_login(finder)
        # Отправка логина и пароля
        send_login_password(finder, login, password, link, count)

        # Подписаться
        click_subscribe_button(finder, login, password, link, count, i)
        sleep(1.5)

        # Открыть меню юзера
        open_menu_user(finder, login, password, link, count)

        # Нажать Выйти
        click_exit_button(finder, login, password, link, count)
        
        # Нажать Войти
        click_login_button(finder, login, password, link, count)

        # Выбрать другой акк
        select_other_acc(finder, login, password, link, count)

        count += 1
        print(f'Proc.{i} подписка завершена, число подписок потока {i}: {count}')
    
    driver.quit()
    print(f'Proc.{i} завершен')



accounts = open_sign() 
links = open_links() 

print('Введите необходимую ссылку. Пример: https://zen.yandex.ru/fitness13')
# link = input('Ввод ссылки: ')
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
average = 0
# print(len(new_accounts))
default_count_threading = threading.activeCount() # для понимания того, сколько потоков запущено изначально
link_complited = 0 # индекесация для листа со ссылками 
while link_complited != len(links): # пока не используем все ссылки

    if default_count_threading == threading.activeCount():
        print('Запускаются новые потоки ...')
        for flows in range(flows_max): # создание потоков
            if second_index == 0:
                average = int(len(new_accounts)/flows_max) # разделение массива на равные части для каждого потока
                second_index = average
            else:
                first_index = second_index
                second_index += average
                # коррекция погрешности при разделении массива
                if (flows == (flows_max-1)) and (second_index != len(new_accounts)):
                    second_index = len(new_accounts) 

            # print(first_index, ':', second_index)
            arr = new_accounts[first_index:second_index] # создание временного массива для передачи в поток
            try:
                threading.Thread(target=subscribing, args=[flows, links[link_complited], arr]).start()
                print(flows, 'поток запущен')
            except:
                print('err')

        first_index = 0
        second_index = 0
        print('\nНачаты потоки')
        print(f'Число потоков сейчас {default_count_threading - threading.activeCount()}')
        print(f'Линк {link_complited + 1} стартует')
        link_complited += 1

    sleep(2)

print('\n\nПрограмма завершена')
pause = input('Введите <Enter> для выхода . . . ')
