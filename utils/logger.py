import logging
from config.app_config import BASE_DIR
import sys

def setupLogger( level=logging.DEBUG):
    name = "System logger"
    log_file = "City_data_fetcher.log"
    logger = logging.getLogger(name)
    if logger.handlers:
        logger.handlers.clear()

    log_dir = BASE_DIR / "logs"
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir/log_file
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger