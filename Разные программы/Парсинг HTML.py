from bs4 import BeautifulSoup
import os

with open('СТАТЬИ.html', 'r', encoding='utf-8') as f:
    html_content = f.read()


soup = BeautifulSoup(html_content, 'html.parser')

# print(soup.find_all('b')) # Название
# print(soup.find_all('i')) # Авторы
# print(soup.find_all('a'))

for y, i in enumerate(soup.find_all('span')):
    try:
        # d = i.span.text
        # print(d)
        # d = i.find_all('font')[1].a

        # d = i.find_all('font')[1]
        # if d is None:
        #     print()
        # else:
        #     print(d)
        d = i.find_all('font')[1].text
        print(d)

    except:
        continue

