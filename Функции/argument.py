# Функция принимает два аргумента в таком порядке: секция и книга
def search(section, book):
    print('Ваша книга: ', section, book)


# Передаём данные в том же порядке
search('История', 'История государства Российского')


def greet(name='Посетитель', message='Привет, '):
    print(message, name)


def print_message(message, name=None):
    if name:
        print(f"{message}, {name}!")
    else:
        print(message)


print_message('Привет', 'Валера')
print_message('Привет')

# Вызов функции без указания значения по умолчанию
greet()  # Вывод: Привет, Посетитель

# Вызов функции с изменённым значением по умолчанию
greet('Артём')  # Вывод: Привет, Артём


# Передача по значению и по ссылке

def add_item(my_list, item):
    # Изменяем переданный список
    my_list.append(item)


numbers = [1, 2, 3]
add_item(numbers, 4)
print(numbers)


# Словарь в качестве аргументов

def print_person_info(**kwargs):
    print(f'Имя: {kwargs.get('name')}')
    print(f'Возраст: {kwargs.get('age')}')


# Передача словаря в качестве именованных аргументов
person_1 = {'name': 'Аня', 'age': 10}
person_2 = {'name': 'Борис'}
person_3 = {'age': 12}
person_4 = {}
print_person_info(**person_1)
