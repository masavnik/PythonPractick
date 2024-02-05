'''СПИСКИ - ИЗМЕНЯЕМЫЙ ТИП ДАННЫХ'''

# 1. Создать список
new_list_one = [98, 32, 48, 1, 121]
new_list_two = ['Лада', 'Волга', 'ГАЗ', 'BMW', 'Mercedes', 'Audi']
new_list = [] # С помощью литерала
new_list_ = list() # С помощью функции


# 2. Доступ к элементам списка
access_element_list_one = new_list_one[0]
# Вывод: 98
access_element_list_two = new_list_two[-1]
# Обращение к элементу отрицательно
# Вывод: Audi

# 3. Срез списка [start:stop:step]
slice_list_one_1 = new_list_one[:3]
# Вывод: [98, 32, 48]
slice_list_one_2 = new_list_one[1:3]
# Вывод: [32, 48]
slice_list_one_3 = new_list_one[1:-1:2]
# Вывод: [32, 1]

# 4. Метод list.index(element) - возвращает положение первого индекса
index_one = new_list_one.index(32)
# Вывод: 1
index_two = new_list_two.index('Mercedes')
# Вывод: 4

# 5. Метод list.count(element) - считает количество раз, когда значение появляется в списке
random_list_one = [4, 1, 5, 4, 10, 4]
random_list_two = ['black', 'red', 'blue', 'oring', 'white', 'white']

count_one = random_list_one.count(4)
# Вывод: 3
count_two = random_list_two.count('white')
# Вывод: 2

# 6. Метод list.sort() - сортирует список
random_list_one.sort()
# Вывод: [1, 4, 4, 4, 5, 10]
random_list_two.sort(reverse=True)
# Вывод: ['white', 'white', 'red', 'oring', 'blue', 'black'] reverse=True - переворачивает список

# 7. Метод list.append(element) - добавляет элемент в конец списка
list_number = [7, 4, 3, 2]
list_str = ['Привет', 'Здравствуйте', 'Добрый день', 'Добрый вечер']
list_str.append('Приветствую')
# Вывод: [7, 4, 3, 2, 44]
list_number.append(44)
# Вывод: ['Привет', 'Здравствуйте', 'Добрый день', 'Добрый вечер', 'Приветствую']

# 8. Метод list.remove(element) - удаляет первое вхождение значения в списке
list_number.remove(2)
# Вывод: [7, 4, 3, 44]
list_str.remove('Привет')
# Вывод: ['Здравствуйте', 'Добрый день', 'Добрый вечер', 'Приветствую']

# 9. Метод list.pop(index) - удаляет элемент по индексу и возвращает элемент
number = [2, 3, 55, 34, 22, 676, 2]
number_index = number.pop(2)
# Вывод: 55

# 10. Метод list.extend(list) - расширяет список, добавляя элементы
num_one = [7, 44, 22, 5]
num_two = [33, 2, 65, 9]
num_one.extend(num_two)
# Вывод: [7, 44, 22, 5, 33, 2, 65, 9]

# 11. Метод list.insert(index, element) - вставляет элемент под указанным индексом
a = [11, 22, 33, 44]
a.insert(3, [55, 66, 77])
# Вывод: [11, 22, 33, [55, 66, 77], 44]