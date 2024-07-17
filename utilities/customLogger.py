import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\ALlLogs.log')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


