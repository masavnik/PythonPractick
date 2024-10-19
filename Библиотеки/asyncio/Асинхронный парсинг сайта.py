import requests
from bs4 import BeautifulSoup as bs
import aiohttp
import asyncio


data_phone = {}


async def all_cat(session, catt):
    for i in [catt]:
        async with session.get(i) as response1:
            response_text = await response1.text()
            soup = bs(response_text, 'html.parser')
            url_phone = soup.find_all('a', class_='cat_item_color')
            phone_categories = ['https://trade59.ru/' + y.get('href') for y in url_phone]
            for y in phone_categories:
                async with session.get(y) as response2:
                    response_text = await response2.text()
                    soup = bs(response_text, 'html.parser')
                    url_phone = soup.find('div', class_='items-list').find_all('a')
                    phone_name_soup = soup.find('div', class_='items-list').find_all('a')
                    main_url_phone = [['https://trade59.ru/' + y.get('href') for y in url_phone][0]]
                    name_phone = [y.get('title') for y in phone_name_soup][0]
                for i_phone in main_url_phone:
                    async with session.get(i_phone) as response3:
                        response_text = await response3.text()
                        soup = bs(response_text, 'html.parser')
                        try:
                            price = soup.find('div', class_='price').find('span').text
                            data_phone[name_phone] = price
                        except AttributeError:
                            data_phone[name_phone] = 'Нет в наличии'


async def all_phone():
    async with aiohttp.ClientSession() as session:
        response = await session.get(url='https://trade59.ru/catalog.html?cid=7')
        soup = bs(await response.text(), 'html.parser')
        url_phone_soup = soup.find_all('a', class_='cat_item_color')

        tasks = []
        url_iphone_main = ['https://trade59.ru/' + i.get('href') for i in url_phone_soup]

        for catt in url_iphone_main:
            task = asyncio.create_task(all_cat(session, catt))
            tasks.append(task)

        await asyncio.gather(*tasks)


# Можно сделать еще быстрее, для этого, каждая сессия в отдельной функции
# Будет создавать другие задачи







print(asyncio.run(all_phone()))
print(data_phone)
