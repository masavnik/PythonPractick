from loguru import logger


logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')  # Запись в файл

logger.debug('Hello world (debug)')
logger.info('Hello world (info)')
logger.error('Hello world (error)')
