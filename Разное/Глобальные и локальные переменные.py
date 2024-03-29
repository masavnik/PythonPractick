def summa():
    a = 10  # Локальная переменная
    b = 20  # Локальная переменная
    c = a + b
    print(f'Сумма: {c} '
          f'Имя функции {summa.__name__}')


summa()
print()
print('#' * 20)
print()


def msg():
    m = "Привет, как дела?"
    print(m)


msg()
m = "Отлично!"  # Глобальная переменная
print(m)
print()
print('#' * 20)
print()
# Правила использования global
# Если значение определено на выходе функции, то оно автоматически станет глобальной переменной.
# Ключевое слово global используется для объявления глобальной переменной внутри функции.
# Нет необходимости использовать global для объявления глобальной переменной вне функции.
# Переменные, на которые есть ссылка внутри функции, неявно являются глобальными.


c = 9


def mul():
    global c
    c = c * 10
    print("Значение в функции:", c)


mul()
print("Значение вне функции:", c)
print()
print('#' * 20)
print()


# Global во вложенных функциях

def add():
    t = 15

    def modify():
        global t
        t = 20

    print("Перед изменением:", t)
    print("Внесение изменений")
    modify()
    t = 40
    print("После изменения:", t)


add()
print("Значение t:", t)
