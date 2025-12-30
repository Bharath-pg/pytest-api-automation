# utils/logger.py
import logging
import sys

def get_logger():
    logger = logging.getLogger("api-tests")
    
    if not logger.handlers:  # To avoid duplicate handlers
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
