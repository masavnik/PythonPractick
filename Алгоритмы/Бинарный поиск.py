

def binary_search(elements: list, s: int):
    low = 0
    high = len(elements) - 1

    while low < high:

        middle = (low + high) // 2
        guess = elements[middle]

        if guess == s:
            return middle
        if guess > s:
            high = middle - 1
            return high
        else:
            low = middle + 1
            return low
    return None




print(binary_search([2, 3, 1, 6, 44, 7, 23, 87, 12], 12))

