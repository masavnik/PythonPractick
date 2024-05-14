import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import pickle


options = webdriver.ChromeOptions()

user_agent = UserAgent()
options.add_argument(f'--user-agent={user_agent.random}')

# Фоновый режим
# options.add_argument('--headless')

driver = webdriver.Chrome()
driver.get('https://www.avito.ru/perm/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&radius=200&searchRadius=200')
# print(driver.window_handles)
print(f'Текущий URL: {driver.current_url}')
sleep(3)


# all_product = driver.find_elements(By.XPATH, '//*[@data-marker="item"]')
all_product = driver.find_elements(By.CLASS_NAME, 'iva-item-title-py3i_')
puge = driver.find_elements(By.XPATH, '//*[@data-marker="pagination-button"]')
# print(driver.window_handles) - Объект вкладки
sleep(2)

all = 0

while True:

    for i in puge:
        i.click()
        sleep(3)
    # a = driver.find_elements(By.CLASS_NAME, 'iva-item-title-py3i_')
    # for y in a:
    #     print(y.text)
    # sleep(3)

# driver.quit()


# def new_window():
#     all_product[0].click()
#     # Переходим на вторую вкладку под индексом 1, так как под индексом 0
#     # у нас находится главная кладка
#     driver.switch_to.window(driver.window_handles[1])
#     print(f'URL открытой вкладки: {driver.current_url}')
#     sleep(3)
#     nameproduct = driver.find_element(By.CLASS_NAME, 'style-titleWrapper-Hmr_5')
#     print(f'Название продукта: {nameproduct.text}')
#     sleep(5)