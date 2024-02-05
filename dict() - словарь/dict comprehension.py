"""dict comprehension"""

new_dict_comp = {n: n**2 for n in range(10) if n % 2 == 0}
#Вывод: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}