class Person:
    @staticmethod
    def info_person(name, surname):
        return f'Меня зовут {name}\n' \
               f'Моя фамилия {surname}'


print(Person.info_person('Владислав', 'Петров'))

# У статического метода нет обязательных параметров SELF
# Доступ к ним можно получить как из экземпляра класса, так и самого класса
