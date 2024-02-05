"""МЕТОДЫ СТРОК"""

# 1. Метод str.isalnum() - состоит ли строка из букв и цифр.
text_1 = 'abracadabra123456'
isalnum_text_1 = text_1.isalnum()
# Вывод: True
text_2 = 'a*b$ra cadabra'
isalnum_text_2 = text_2.isalnum()
# Вывод: False

# 2. Метод str.replace() используются для замены символов или подстрок.
name_surname = 'Олех Петрох'
name_surname_replace = name_surname.replace('х', 'г', 1)
# Вывод: Олег Петрох
# Заменяем вторую букву
name_surname1 = 'Олех Петрох'
name_surname_replace1 = name_surname.replace('х', 'г', 1).replace('х', 'в', 1)
# Вывод: Олег Петров

# 3. Метод str.partition() поможет преобразовать строку в кортеж.
text3 = 'Привет, как у тебя дела?'
text3_partition = text3.partition(' как ')
# Вывод: ('Привет,', ' как ', 'у тебя дела?')

# 4. Метод str.isalpha() состоит ли строка только из букв, или включает специальные символы.
text_prog = 'программирование'
text_prog_isalpha = text_prog.isalpha()
# Вывод: True

text_prog_num = 'программирование123%^'
text_prog_num_isalpha = text_prog_num.isalpha()
# Вывод: False

# 5. Метод str.isdigit() входят ли в строку только цифры, или там есть и другие символы.
str_num1 = '123456789'
str_num1_isdigit = str_num1.isdigit()
# Вывод: True
str_num2 = '123456789d'
str_num2_isdigit = str_num2.isdigit()
# Вывод: False

# 5. 