class Car:
    def __call__(self, a, b):
        return a * b


car = Car()

print(car(2, 4))