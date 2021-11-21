import logging


class LogGenerator:
    @staticmethod
    def logInfoGenerator():

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename=".\\Logs\\automation.log",
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
