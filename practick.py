import requests
from routingpy import MapboxOSRM
from routingpy import Valhalla
from pprint import pprint


x = '37.5760782'
y = '55.68263049999999'

a = f'http://routing.digimap.ru/directions?%7B%22guid%22:%2284604758-B176-4D9F-B1C1-0036D8DAAED0%22,%22speed%22:%22max%22,%22points%22:[%7B%22x%22:{x},%22y%22:{y}%7D,%7B%22x%22:37.617711,%22y%22:55.755811%7D],%22vehicles%22:%7B%22publicTransportRoute%22:%7B%7D,%22pedestrian%22:%7B%7D%7D%7D'

d = f'http://routing.digimap.ru/directions?%7B%22guid%22:%2284604758-B176-4D9F-B1C1-0036D8DAAED0%22,%22speed%22:%22max%22,%22points%22:[%7B%22x%22:{x},%22y%22:{y}%7D,%7B%22x%22:37.617711,%22y%22:55.755811%7D],%22vehicles%22:%7B%22car%22:%7B%7D%7D%7D'


c = requests.get(a).json()
f = requests.get(d).json()

print(int(c['properties']['length']))
print(int(c['properties']['time']))
print()
print(int(f['properties']['length']))
print(int(f['properties']['time']))