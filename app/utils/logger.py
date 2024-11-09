import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('food_delivery_app')
    return logger
