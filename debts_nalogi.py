from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
try:
    inn_search = int(input('Введите ИНН: '))

    params = {'inn':f'{inn_search}'}
    print('\nИдет поиск по nalogi.online ...')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f'https://nalogi.online/?query={inn_search}')
    try:
        debts = driver.find_element(By.CLASS_NAME, 'debt.ng-scope.checked.single').text
        result_debts, ru = debts.split(' ')
        print(f'Задолженность {result_debts} | Источник: nalogi.online')
    except:
        print(f'Налоговой задолженности по ИНН {inn_search} не найдено')
except ValueError:
    print('Нужно ввести цифры')


