'''Полиморфизм'''
# С каждым объектом работаем одинаково, но каждый объект ведет себя по разному
# Возможность обработки совершенно разных объектов, путем использования одного
# и того же метода по названию


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Площадь - ПРЯМОУГОЛЬНИКА {s}, Размеры a - {x} b - {y}'.format(s=self.get_area(),
                                                                              x=self.a,
                                                                              y=self.b
                                                                              )

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return 'Площадь КВАДРАТА - {s}, Размеры: a - {x}'.format(s=self.get_area(),
                                                                 x=self.a
                                                                 )

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return 'Площадь КРУГА - {s}, Размеры: r - {x}'.format(s=self.get_area(),
                                                              x=self.r
                                                              )

    def get_area(self):
        return 3.14 * self.r ** 2


rec1 = Rectangle(4, 9)
rec2 = Rectangle(5, 11)

squ1 = Square(4)
squ2 = Square(5)

cir1 = Circle(10)
cir2 = Circle(8)

figures = [rec1, rec2, squ1, squ2, cir1, cir2]

for i_fig, y_fig in enumerate(figures):
    print(i_fig + 1, y_fig)
