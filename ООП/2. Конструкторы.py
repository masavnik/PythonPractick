# Конструктор — это специальный метод, который вызывается по умолчанию когда вы создаете объект класса.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        if self.age < 14:
            return f'Меня зовут {self.name} {self.surname} и мне {self.age} годиков'
        else:
            return f'Меня зовут {self.name} {self.surname} и мне {self.age} лет'


person = Person('Олег', 'Хромцов', 12)


class Car:
    count = 0

    def __init__(self):
        Car.count += 1
        print(Car.count)


car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()

