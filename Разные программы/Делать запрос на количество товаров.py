import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


for index, row in df.iterrows():
    if index > 2759:
        try:
            str_swap = str(row[1]).replace(' ', '%20')
            url = f'https://www.wildberries.ru/catalog/0/search.aspx?search={str_swap}'
            # c = 'https://www.wildberries.ru/catalog/0/search.aspx?search=швабра%20с%20отжимом'
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_experimental_option("detach", True)
            browser = webdriver.Chrome(options=options)
            sleep(3)
            browser.get(url)
            sleep(3)
            count_product = browser.find_element(By.CLASS_NAME, 'searching-results__inner')
            print(index, ''.join([i for i in count_product.text if i.isdigit()]), url)
        except:
            print()
            continue


