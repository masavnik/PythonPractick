
def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        j = i -1

        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_value

array = [3, 7, 2, 1, 8, 4, 5]
insertion_sort(array)
print(array)