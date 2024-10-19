import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import pickle


name_user = 'standard_user'
password = 'secret_sauce'

options = webdriver.ChromeOptions()

user_agent_list = [
    'hello',
    'world',
    'home'
] # Здесь могу быть юзер агенты для тестирования

# Меняем юзер агента
user_agent = UserAgent()
# options.add_argument('--user-agent=Mozilla/5.0 (Android 10; Mobile; rv:122.0) Gecko/122.0 Firefox/122.0')
# options.add_argument(f'--user-agent={random.choice(user_agent_list)}')
options.add_argument(f'--user-agent={user_agent.random}')
# Прокси
# options.add_argument('--proxy-server=90.151.34.107:8000')
# Отключения webdriver, чтобы быть похожим на реальных пользователей
options.add_argument('--disable-blink-features=AutomationControlled')
# Фоновый режим
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.saucedemo.com/')

# Находим элемент для вставки name_user
input_user = driver.find_element(By.XPATH, '//*[@id="user-name"]')
input_user.send_keys(name_user) # Вставляем значение name_user в форму

# Находим элемент для вставки password
input_password = driver.find_element(By.XPATH, '//*[@id="password"]')
input_password.send_keys(password) # Вставляем значение password в форму
sleep(2)
# input_password.send_keys(Keys.ENTER) # После ввода пароля нажимаем Enter для входа
# Находим элемент кнопки Login(на сайте)
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click() # Кликаем на кнопку, чтобы войти на сайт
#
############################################################
#
# Запись данных для повторного входа
pickle.dump(driver.get_cookies(), open(f'{name_user}cookies', 'wb'))

############################################################

# Запускаем заного
# driver.get('https://www.saucedemo.com/')
#
# for cookie in pickle.load(open(f'{name_user}cookies', 'rb')):
#     driver.add_cookie(cookie)
#
# sleep(4)
# driver.refresh()

############################################################

sleep(10)

driver.quit()