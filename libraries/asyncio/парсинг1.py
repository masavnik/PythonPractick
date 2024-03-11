import requests
from bs4 import BeautifulSoup as bs


def get_data(url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    url_phone_soup = soup.find_all('a', class_='cat_item_color')

    url_iphone_main = ['https://trade59.ru/' + i.get('href') for i in url_phone_soup]
    data_phone = {}
    for i in url_iphone_main:
        response = requests.get(i)
        soup = bs(response.content, 'html.parser')
        url_phone = soup.find_all('a', class_='cat_item_color')
        phone_categories = ['https://trade59.ru/' + y.get('href') for y in url_phone]

        for y in phone_categories:
            response = requests.get(y)
            soup = bs(response.content, 'html.parser')
            url_phone = soup.find('div', class_='items-list').find_all('a')
            phone_name_soup = soup.find('div', class_='items-list').find_all('a')
            main_url_phone = [['https://trade59.ru/' + y.get('href') for y in url_phone][0]]
            name_phone = [y.get('title') for y in phone_name_soup][0]

            for i_phone in main_url_phone:
                response = requests.get(i_phone)
                soup = bs(response.content, 'html.parser')
                try:
                    price = soup.find('div', class_='price').find('span').text
                    data_phone[name_phone] = price
                except AttributeError:
                    data_phone[name_phone] = 'Нет в наличии'

    return data_phone


def main():
    print(get_data(url='https://trade59.ru/catalog.html?cid=7'))


if __name__ == '__main__':
    main()
