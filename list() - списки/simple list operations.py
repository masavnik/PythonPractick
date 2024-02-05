'''ПРОСТЫЕ ОПЕРАЦИИ НАД СПИСКАМИ'''

new_list_one = [98, 32, 48, 1, 121]
new_list_two = ['Лада', 'Волга', 'ГАЗ', 'BMW', 'Mercedes', 'Audi']
number_list = [1, 2, 3, 4]

# 1. True если элемент 1 находится в списке new_list_one
element_true = 1 in new_list_one
# Вывод: True

# 2. False если элемент volvo не находится в списке new_list_two
element_false = 'volvo' in new_list_one
# Вывод: False

# 3. False если элемент text не находится в списке new_list_two
number = 98
exam_one = number not in new_list_one
# Вывод: False

# 4. True если элемент number не находится в списке new_list_one
text = 'volvo'
exam_two = text not in new_list_two
# Вывод: True

# 5. Объединение списков
general = new_list_one + number_list
# Объединять можно разные типы данных, но лучше в списке хранить один тип
# Вывод: [98, 32, 48, 1, 121, 1, 2, 3, 4]

# 6. Количество элементов списка
list_len = len(new_list_one)
# Вывод: 5

# 7. Самый большой элемент списка
list_max = max(new_list_one)
# Вывод: 121

# 8. Наименьший элемент списка
list_min = min(new_list_one)
# Вывод: 1

# 9. Сумма чисел в списке
list_sum = sum(new_list_one)
# Вывод: 300

# 10. Генератор списков python (list comprehension)
# Более подробно в файле list comprehensions.py
x = [i for i in range(10)]
# Вывод: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 11. list.reverse() - разворачивает список
x.reverse()
# Вывод: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 12. * копирует элементы в списке
list4 = [1, 2, 3, 4]
list5 = list4 * 3
# Вывод: [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]