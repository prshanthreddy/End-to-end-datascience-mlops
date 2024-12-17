import os
import sys
import logging

# Define the logging format
#can also use logging_str = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s  - %(name)s - %(message)s"
logging_str = "[%(asctime)s] %(levelname)s - %(module)s - %(message)s"

# Define the directory and file path for the log file
log_dir = "logs"
log_file_path = os.path.join(log_dir, "logging.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger object
logger = logging.getLogger("datascience_logger")
