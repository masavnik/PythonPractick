
def gen():
    for i in range(0, 10):
        yield i


def add(*args):
    print(args)
    print(sum(args))


l = [1, 3, 5, 3]
add(*l)


def task2(*args, **kwargs):
    print(args)
    print(kwargs)


task2(1, 2, 4, 2, street='lenina', sity='perm ')
