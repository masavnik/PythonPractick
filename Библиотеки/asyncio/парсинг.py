import aiohttp
import asyncio
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import requests
import csv

BASE_URL = 'https://trade59.ru/'
CATALOG_URL = 'https://trade59.ru/catalog.html'
USER_AGENT = {'User-Agent': UserAgent().random}


async def get_data_cat(session, cat_url):
    async with session.get(cat_url) as response:
        response_text = await response.text()

        soup = BS(response_text, 'html.parser')
        all_data = soup.find_all('a', {'class': 'cat_item_color'})

        for al in all_data:
            print(BASE_URL + al['href'], al.text.strip())



async def all_categories():
    async with aiohttp.ClientSession() as session:  # Позволяет создать сессию
        r = await session.get(CATALOG_URL, headers=USER_AGENT)
        soup = BS(await r.text(), 'html.parser')
        categories = soup.find_all('a', {'class': 'cat_item_color'})
        link_cat = [BASE_URL + cat_i['href'] for cat_i in categories]
        tasks = []
        for cat in link_cat:
            task = asyncio.create_task(get_data_cat(session, cat))
            tasks.append(task)

        await asyncio.gather(*tasks)


async def main():
    await all_categories()


if __name__ == '__main__':
    asyncio.run(main())


class ParsingTrade:
    def __init__(self, url):
        self.url = url
        # self.categories = self.get_categories()

    @staticmethod
    def fetch(url):
        response_url = requests.get(url)
        return BS(response_url.content, 'html.parser')

    def get_data_product(self, url_product):
        response = self.fetch(url_product)
        price = response.find('div', class_='price').find('span').text
        name = response.find('main', class_='content-in').find('h1').text
        description = response.find('div', class_='descript1').text.replace(f';{" "}', '\n').strip()
        return {
            'Название': name.strip(),
            'Цена': price,
            'Описание': description
        }

    def get_product_color(self, url_product_color):
        response = self.fetch(url_product_color)
        color_find = response.find('div', class_='items-rows')
        color_list = color_find.find_all('a')[::3]
        return {
            i['title']: self.url + i['href'][12:] for i in color_list
        }

    def get_product_memery(self, url_product_memory):
        response = self.fetch(url_product_memory)
        all_memory = response.find_all('a', class_='cat_item_color')
        return {
            i['title']: self.url + i['href'][12:] for i in all_memory
        }

    def get_all_product(self, url_all_product):
        response = self.fetch(url_all_product)
        all_product = response.find_all('a', 'cat_item_color')
        return {
            i['title']: self.url + i['href'][12:] for i in all_product
        }

    def parse(self):
        self.crete_csv()
        with open('trade59.csv', 'a', newline='', encoding='utf-8') as file:

            for i in self.get_all_product('https://trade59.ru/catalog.html?cid=7').items():
                for y in self.get_product_memery(i[1]).items():
                    for t in self.get_product_color(y[1]).items():
                        try:
                            writer = csv.writer(file)
                            writer.writerow([t[0], self.get_data_product(t[1])['Цена'], t[1],
                                             ])
                        except AttributeError:
                            writer.writerow([t[0], 'Нет в наличии', t[1]])

    def crete_csv(self):
        with open('trade59.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Ссылка'])

# main_trade = ParsingTrade('https://trade59.ru/catalog.html')
# a = main_trade.parse()
# print(a)
