import logging

def setup_logger(name):
    """Set up and return a logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        fh = logging.FileHandler('floodzap.log')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger

# Create a logger instance for the application
app_logger = setup_logger('FloodZap')

def log_request(data):
    """Log incoming requests."""
    app_logger.info(f"Request: {data}")

def log_response(data):
    """Log outgoing responses."""
    app_logger.info(f"Response: {data}")