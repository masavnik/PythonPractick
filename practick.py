
list_one = ['Масальских', 'Петров', 'Хромцов', 'Иванов', 'Куц']
list_two = ['Владислав', 'Олег', 'Игорь', 'Евгений', 'Алексей']


for i in range(len(list_one)):
    for y in range(len(list_one) + 1):
        if len(list_one[y]) > len(list_one[y]) + 1:
            list_one[y], list_one[y + 1] = list_one[y + 1], list_one[y]

print(list_one)