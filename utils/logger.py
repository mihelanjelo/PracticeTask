import logging


class Logger:

    instance = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('log/test.log')
        c_handler.setLevel(logging.INFO)
        f_handler.setLevel(logging.INFO)
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)
        self.logger.setLevel(logging.INFO)

    def debug(self, step):
        self.logger.debug(step)

    def info(self, step):
        self.logger.info(step)

    def warning(self, step):
        self.logger.warning(step)

    def error(self, step):
        self.logger.error(step)

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Logger()
        return cls.instance
