import requests
from bs4 import BeautifulSoup as bs


def writer_html():
    '''Запись html в файл'''
    response = requests.get('https://quotes.toscrape.com/')
    soup = bs(response.content, 'html.parser')

    with open('example.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))


def get_example(site_file):
    with open(site_file, 'r', encoding='utf-8') as file:
        soup = bs(file.read(), 'html.parser')
        # Tag
        tag_one = soup.link
        tag_two = soup.div.div.a
        print()
        # Name
        name_atrebute = tag_one['rel']  # Получение атрибута
        teg_attrs = tag_one.attrs  # Получение словаря атрибутов
        print()
        print(soup)


def get_data_site(file):
    '''Получение ссылок лучших цитат'''
    with open(file, 'r', encoding='utf-8') as f:
        soup = bs(f.read(), 'html.parser')

        best_mess_find = soup.find('div', class_='col-md-4 tags-box')
        best_mess_find_all = best_mess_find.find_all('span')
        for i in best_mess_find_all:
            print('https://quotes.toscrape.com' + i.a['href'])


get_data_site('example.html')
