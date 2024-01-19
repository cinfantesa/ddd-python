import logging

from infrastructure.logging.logger import Logger


class JsonLogger(Logger):
    def info(self, message: str) -> None:
        logging.basicConfig(level=logging.INFO, format='{"dateTime": "%(asctime)s", "level": "info", "message": "%(message)s"}',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info(message)
