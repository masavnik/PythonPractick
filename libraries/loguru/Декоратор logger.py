from loguru import logger

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='10 KB', compression='zip')


def divide(a, b):
    return a / b

@logger.catch
def main():
    divide(1, 0)


if __name__ == '__main__':
    main()