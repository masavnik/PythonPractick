
def quick_sort(array_sorted):
    if len(array_sorted) < 2:
        return array_sorted
    else:
        pivot = array_sorted[0]
        less = [num for num in array_sorted[1:] if num <= pivot]
        greater = [num for num in array_sorted[1:] if num > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

array = [3, 56, 23, 55, 7, 4, 8]
sorted_arr = quick_sort(array)

print(sorted_arr)