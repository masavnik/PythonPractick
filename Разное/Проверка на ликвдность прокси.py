import requests

with open('proxy.txt', 'r') as file:
    proxi = ''.join(file.readlines()).strip().split('\n')

for i_proxi in proxi:
    proxies = {
        'http': f'http://{i_proxi}',
        'https': f'http://{i_proxi}'
    }

    link = 'https://allegro.pl/'

    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {response}')
    except:
        print(proxi, 'Прокси не валидный')