import logging
import os
from src.configs.app import settings  # ваш модуль с настройками


def setup_logger():
    logger = logging.getLogger("Менеджер-бот")
    logger.setLevel(logging.DEBUG)  # Общий уровень логгирования

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if settings.MODE == 'DEV':
        # Обработчик вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    elif settings.MODE == 'PROD':
        # Директория для логов
        log_dir = '/path/to/log/directory'  # Замените на фактический путь
        os.makedirs(log_dir, exist_ok=True)  # Создаёт директорию, если её нет

        # Обработчик записи в файл
        file_handler = logging.FileHandler(os.path.join(log_dir, 'error.log'))
        # Логируем только ошибки и критические сообщения
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.propagate = False
    return logger


logger = setup_logger()
