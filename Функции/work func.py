def name_func(arg):
    one_p = f'name_func - тело функции'
    two_p = f'{arg} - фргумент - ы'

    return one_p, two_p


def summ(a, b):
    return a + b


def make_counter():
    # Объявляем переменную count в объемлющей функции
    count = 0

    def counter():
        # Указываем, что count находится в объемлющей функции
        nonlocal count
        count += 1
        return count

    return counter

# Создаём счётчик
call_counter = make_counter()
print(call_counter())  # Вывод: 1
print(call_counter())  # Вывод: 2
print(call_counter())  # Вывод: 3


# Глобальная переменная, которая обозначает количество сделанных тортов
cake_count = 10

def modify_cake():
    global cake_count
    # Изменяем значение глобальной переменной
    cake_count = 15
    return cake_count

modify_cake()
print(modify_cake())  # Вывод: 15