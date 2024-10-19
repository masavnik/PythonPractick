import os

print(f'Текущая деректория: {os.getcwd()}')

# Создание папки
if not os.path.isdir("test"):
    os.mkdir("test")

# Изменение директории
os.chdir("test")
print(f'Текущая деректория: {os.getcwd()}')

# вернуться в предыдущую директорию
os.chdir("..")
# сделать несколько вложенных папок
os.makedirs("nested1/nested2/nested3")

# Переименование файлов
# переименовать text.txt на renamed-text.txt
os.rename("text.txt", "renamed-text.txt")

# Перемещение файлов
# заменить (переместить) этот файл в другой каталог
os.replace("renamed-text.txt", "folder/renamed-text.txt")

# Список файлов и директорий
print("Все папки и файлы:", os.listdir())

# распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))


# удалить этот файл
os.remove("folder/renamed-text.txt")

# удалить папку
os.rmdir("folder")

open("text.txt", "w").write("Это текстовый файл")

# вывести некоторые данные о файле
print(os.stat("text.txt"))


# например, получить размер файла
print("Размер файла:", os.stat("text.txt").st_size)