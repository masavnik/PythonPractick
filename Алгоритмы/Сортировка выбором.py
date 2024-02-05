
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

array = [2, 4, 1, 88, 44, 66 ,4, 9]
selection_sort(array)

print(array)