import logging
import os

# --> Create logs folder
os.makedirs("logs", exist_ok=True)

# --> Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("financecore_logger")

# --> INFO LOG
def log_info(message):
    logger.info(message)

# --> WARNING LOG
def log_warning(message):
    logger.warning(message)

# --> ERROR LOG
def log_error(message):
    logger.error(message)