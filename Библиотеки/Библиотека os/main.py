import os


print(f'Текущая директория: {os.getcwd()}')

# Создать новую директорию
os.mkdir(f'holder')

# повторный запуск mkdir с тем же именем вызывает FileExistsError,
# вместо этого запустите:
try:
     os.mkdir(f'holder')
except FileExistsError as ex:
     print(ex)



# изменение текущего каталога на 'folder'
os.chdir("folder")

print("Текущая директория изменилась на folder:", os.getcwd())

# Создание вложенных папок
# вернуться в предыдущую директорию
os.chdir("..")

# сделать несколько вложенных папок
os.makedirs("nested1/nested2/nested3")

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

# удалить вложенные папки
os.removedirs("nested1/nested2/nested3")

# Посмотреть информацию о файлах
open("text.txt", "w").write("Это текстовый файл")

# вывести некоторые данные о файле
print(os.stat("text.txt"))