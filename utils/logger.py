import logging


def setup_logger(name, log_file, level=logging.INFO):
    # Create a formatter with the correct placeholders
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Create a stream handler (console handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Get the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


test_logger = setup_logger('test_logger', 'test.log')
