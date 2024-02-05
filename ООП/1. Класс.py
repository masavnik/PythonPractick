class Car:
    '''Класс Car'''

    # Атрибуты - свойства класса
    brand = 'mercedes'
    model = 'c200'
    release = 2011

    # Метод класса
    def info_car(self):
        return f'Марка: {self.brand}\n' \
               f'Модель: {self.model}\n' \
               f'Год выпуска: {self.release}'

    # Метод класса
    def start_car(self):
        return 'Заводим двигатель'

    # Метод класса
    def stop_car(self):
        return 'Заглушаем двигатель'


# Создали два объекта класса Car
car_one = Car()
car_two = Car()

# Обращаемся к атрибутам и методам класса
print(car_one.release)
print(car_one.start_car())

# Атрибуты класса
print(dir(car_two))



