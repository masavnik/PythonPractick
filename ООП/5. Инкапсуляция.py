'''
Соглашение между программистами
Скрытие данных
'''

class Person:
    # сокрытие данных
    __count = 0  # За пределами класса становится невидимым, внутри класса видимый

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.__count += 1

    def __str__(self):
        return 'Имя: {}\nВозраст: {}'.format(self.__name, self.__age)

    def get_count(self):  # геттер обращаться к атрибутам
        return self.__count

    def get_age(self):  # геттер обращаться к атрибутам
        return self.__age

    def set_age(self, age):  # сеттер обращаться к атрибутам
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Не допустимый возраст')


vlad = Person('Влад', 23)
oleg = Person('Олег', 34)
print(vlad.get_age())
print(oleg.get_age())

new_age = 1
oleg.set_age(new_age)
print(oleg.get_age())
