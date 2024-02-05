import requests
from bs4 import BeautifulSoup as bs

link = 'https://hidemy.io/ru/proxy-list/'


response = requests.get(link)
print(response)
soup = bs(response.content, 'lxml')

find_tbody = soup.find_all('div', class_='services_proxylist')
print(find_tbody)
list_proxy = []

for i in find_tbody:
    print(i)
#     find_proxy = str(i.find('code'))
#     str_proxy = find_proxy.replace('<code>', '').replace('</code>', '\n')
#     if str_proxy != '-1':
#         list_proxy.append(str_proxy)
#         # with open('proxy.txt', 'w') as file:
#         #     file.write(str_proxy)
#
# with open('proxy.txt', 'w') as file:
#     file.writelines(list_proxy)