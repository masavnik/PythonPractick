import random

num = random.randrange(0, 101, 2)
print(f'Диапазон от нуля до 101 с шагом 2 - {num}')

num1 = random.randint(0, 101)
print(f'Диапазон от 0 до 101 - {num1}')

cho = random.choice(['привет', 'что', 'как', 'зачем'])
print(f'Случайный элемент из последовательности - {cho}')

cho1 = random.choices(["яблоки", "бананы", "вишня"], weights=[10, 1, 1], k=5)
print(cho1)

a = ['привет', 'что', 'как', 'зачем']
random.shuffle(a)
print(f'Перемешка последовательности - {a}')

b = random.sample([0, 1, 2, 3, 4, 5, 6], 3)
print(f'Возвращение списка длиной К уникальных элементов - {b}')

print(f'Случайное число {random.random()}')

i = random.uniform(2.5, 10.0)
print(f'Случайное число с плавающей точкой {i}')

print(random.triangular(20, 60, 30))
print(random.betavariate(5, 10))
print(random.expovariate(1.5))
print(random.gammavariate(5, 10))
print(random.gauss(100, 50))
print(random.normalvariate(100, 50))
print(random.vonmisesvariate(1, 4))
print(random.paretovariate(3))
print(random.weibullvariate(1, 1.5))