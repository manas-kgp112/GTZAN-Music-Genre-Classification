# Importing Libraries
import os
import sys
import logging
from datetime import datetime



'''
    This script deals with custom logging feature inherting the standard logging module
    (No need to seprately import CustomLogging module)
'''

# variables to setup logging
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_str = "[%(asctime)s : %(lineno)d : %(name)s : %(levelname)s : %(module)s : %(message)s]"
log_dir = os.path.join(os.getcwd(), "logs", LOG_FILE)
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# creating logs folder
os.makedirs(log_dir, exist_ok=True)

# saving/generating logs
logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("musicClassifierLogger")

