import requests
from bs4 import BeautifulSoup as bs


response = requests.get('https://akb.ru/podbor/toyota/')
print(response.text)