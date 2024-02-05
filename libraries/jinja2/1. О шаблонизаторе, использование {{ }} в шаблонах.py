from jinja2 import Template

# example 1
name = 'Vladislav'
age = 28

tm = Template('My {{ a*2 }} age and name {{ name.upper() }}')
msg = tm.render(name=name, a=age)
print(msg)

# example 2
class Person:
    def __init__(self, name1, age2):
        self.name1 = name1
        self.age2 = age2


person = Person('Владислав', 28)

temp = Template('Мне {{ p.age2 }} лет и зовут {{ p.name1 }}')
ms = temp.render(p=person)
print(ms)

# example 3
auto = {'brand': 'LADA', 'model': '2114', 'speed': '120'}

t = Template('Автомобиль {{ car["brand"] }} {{ car["model"] }} едет со скоростью {{ car["speed"] }}')
m = t.render(car=auto)
print(m)

