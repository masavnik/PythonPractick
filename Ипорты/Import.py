# Импорт os
import os
# Импорт все из модуля datetime, не обращаясь к datetime
from datetime import *
# Импортировать isqrt из библиотеки math с обновлением qrt
from math import isqrt as qrt


def input_age(age):
    if age < 20:
        return 'Ты еще маленький'
    else:
        return f'Добро пожаловать, тебе {age} лет'


data = date.today()
dirct = os.getcwd()
num = qrt(16)
