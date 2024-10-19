import datetime

# Текущая дата
a = datetime.date.today()
print(f'Текущая дата: {a}')

# Создание объека для заданной даты
b = datetime.date(2022, 8, 23)
print(f'Заданная дата: {b}')

# Получение года, месяца и дня для даты
print(f'Год: {b.year}')
print(f'Месяц: {b.month}')
print(f'День: {b.day}')

# Получение лаиы сегодняшнего дня плюс 1 день
c = datetime.date.today() + datetime.timedelta(days=1)
print(f'Завтрашняя дата: {c}')

# Получение разницы между двумя датами
d1 = datetime.date(2021, 1, 1)
d2 = datetime.date.today()
delta = d2 - d1
print(f'Прошло дней: {delta.days}')