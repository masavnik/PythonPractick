'''СЛОВАРЬ - ИЗМЕНЯЕМЫЙ ТИП ДАННЫХ'''

# 1. Создать словарь
new_dict_one = {1: 'one', 2: 'two'}
new_dict_two = dict({1: 'один', 2: 'два'})
dict_sample = dict([(1, 'mango'), (2, 'pawpaw')])

# 2. Доступ к элементам
dict_auto = {'lada': 'vesta',
             'bmw': '750',
             'audi': 'Q7',
             'Mercedes': 'E-class'
             }

lada = dict_auto['lada']
# Вывод: vesta
bmw = dict_auto['bmw']
# Вывод: 750

# 3. Метод dict.get(key) - доступ к элементу
audi = dict_auto.get('audi')
# Вывод: Q7
mercedes = dict_auto.get('Mercedes')
# Вывод: E-class

# 4. Добавление элементов
new_dict_number = {}
new_dict_number[1] = 'один'
new_dict_number[2] = 'два'
new_dict_number[10] = '8', '+', '2'
# Вывод: {1: 'один', 2: 'два', 10: ('8', '+', '2')}

# 5. Обновление элементов
new_dict_number[10] = 'десять'
# Вывод: {1: 'один', 2: 'два', 10: 'десять'}

# 6. Удаление элементов
del new_dict_number[1]
# Вывод: {2: 'два', 10: 'десять'}

# 7. Функция dict.pop(key) удаляет запись в словаре
dict_name = {'Alex': 23, 'George': 20, 'Elena': 31}
alex = dict_name.pop('Alex')
# Вывод: {'George': 20, 'Elena': 31}
# 23

# 8. Функция dict.popitem() удаляет последний элемент в словаре
last_element = dict_name.popitem()
# Вывод: {'George': 20}
# ('Elena', 31)

# 9. Метод len(dict) - можно посчитать количество элементов в словаре
dict_name_1 = {'Alex': 23, 'George': 20, 'Elena': 31}
len_dict = len(dict_name_1)
# Вывод: 3

# 10. Метод dict.copy() - возвращает копию словаря
x = dict_name_1.copy()
# Вывод: {'Alex': 23, 'George': 20, 'Elena': 31}

# 11. Метод dict.items() - возвращает итерируемый объект
# Метод используется, когда нужно перебрать значения словаря.
for i, y in dict_name_1.items():
    print(i, y)
# Вывод: Alex 23
#        George 20
#        Elena 31
for i in dict_name_1.items():
    print(i)
# Вывод: ('Alex', 23)
#        ('George', 20)
#        ('Elena', 31)
dict_items = dict_name_1.items()
# Вывод: dict_items([('Alex', 23), ('George', 20), ('Elena', 31)])

# 12. Метод dict.fromkeys(keys, values) - метод возвращает словарь с указанными ключами и значениями.
list_auto = ['lada', 'volvo', 'bmw']
ls = 2
dict_auto_1 = dict.fromkeys(list_auto, ls)
# Вывод: {'lada': 2, 'volvo': 2, 'bmw': 2}

# 13. Метод dict.setdefault(key, value) - когда нужно получить значение элемента с конкретным ключом
key_name = dict_name_1.setdefault('Валерий', 43)
# Вывод: {'Alex': 23, 'George': 20, 'Elena': 31, 'Валерий': 43}, 43
key_name_1 = dict_name_1.setdefault('Elena', 22)
# Вывод: {'Alex': 23, 'George': 20, 'Elena': 31, 'Валерий': 43}

# 14. Метод dict.keys() - Возвращает список ключей словаря
key_dict_name = dict_name_1.keys()
# Вывод: dict_keys(['Alex', 'George', 'Elena', 'Валерий'])

# 15. Метод dict.values() – получение всех значений элементов словаря
values_name = dict_name_1.values()
# Вывод: dict_values([23, 20, 31, 43])

# 16. Сложение словарей в один
update_dict = dict_name_1 | dict_auto_1
# Вывод: {'Alex': 23, 'George': 20, 'Elena': 31, 'Валерий': 43, 'lada': 2, 'volvo': 2, 'bmw': 2
print('ghbdtn')