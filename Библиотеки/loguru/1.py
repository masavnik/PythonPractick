from loguru import logger


logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='10 KB', compression='zip')

for _ in range(1000):
    logger.debug('Hello world (debug)')

# Запись в файлы, если файл больше 10 KB, то файлы будут зиповаться