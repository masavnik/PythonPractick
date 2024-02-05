def a(num):
    if num == 1:
        return 1
    else:
        return num + a(num - 1)

print(a(7))