import csv


def example_one():
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Имя", "Класс", "Возраст"])
        file_writer.writerow(["Женя", "3", "10"])
        file_writer.writerow(["Саша", "5", "12"])
        file_writer.writerow(["Маша", "11", "18"])


def example_two():
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        names = ["Имя", "Возраст"]
        file_writer = csv.DictWriter(w_file, delimiter = ",",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
        file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
        file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


def example_three():
    csv.register_dialect('my_dialect', delimiter=':', lineterminator="\r")
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, 'my_dialect')
        file_writer.writerow(["Имя", "Класс", "Возраст"])
        file_writer.writerow(["Женя", "3", "10"])
        file_writer.writerow(["Саша", "5", "12"])
        file_writer.writerow(["Маша", "11", "18"])


def example_for():
    '''Если нужно записать несколько списков'''
    titles = ['аываыв', 'афц', 'аывп', 'пывп']
    main_news = ['1', '2', '3', '4']
    img_link = ['гнек', 'цук', 'цукцу', 'нкен']
    text = ['уцка', 'торап', 'рапра', 'рварв']
    with open('news.csv', 'a', newline='', encoding='utf-8') as file_l:
        writers = csv.writer(file_l)
        for i in range(len(titles)):
            row = [titles[i], main_news[i], img_link[i], text[i]]
            writers.writerow(row)