import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object
    logger.setLevel(logging.CRITICAL)
    logger.info("This is info")
    logger.warning("This is warning")
    logger.error("This is error")
    logger.debug("This is error")

    logger.critical("This is critical")
