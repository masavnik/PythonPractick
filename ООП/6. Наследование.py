'''Наследование'''


class Person:
    count = 0

    def __init__(self, name, surname, age, prof):
        self.name = name
        self.surname = surname
        self.age = age
        self.prof = prof
        self.zp = None
        Person.count += 1

    def __str__(self):
        zap = 'Зп не получаю' if self.zp is None else 'Моя зп {}'.format(self.zp)
        choice_prof = 'учусь' if self.prof == 'студент' else 'работаю'

        return 'Меня зовут {0} {1} мне {2}, Я {3}, {4}'.format(self.name,
                                                               self.surname,
                                                               self.age,
                                                               choice_prof,
                                                               zap
                                                               )


class Manager(Person):
    def __init__(self, name, surname, age, prof, zp):  # Данные Класса Manager
        super().__init__(name, surname, age, prof)  # Данные родительского класса
        self.zp = zp


class Student(Person):
    def __init__(self, name, surname, age, prof):  # Данные Класса Student
        super().__init__(name, surname, age, prof)  # Данные родительского класса

    def get_estimates(self, item):
        item_dict = {'Математика': 5, 'Русский язык': 4, 'Информатика': 5, 'Биология': 3, 'Физика': 5}
        if item not in item_dict:
            return 'Такого предмета нет'
        else:
            return 'Оценка по {}: {}'.format(item,
                                             item_dict[item]
                                             )


manager = Manager('Владислав', 'Петров', 22, 'Менеджер', 20000)
print(manager)
student = Student('Олег', 'Петров', 19, 'студент')
print(student)
print(student.get_estimates('Математика'))
print(student.count)
