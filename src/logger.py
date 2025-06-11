# # Any execution that happens , it should all be log/store in some files .
# import logging
# import os
# from datetime import datetime

# logFile = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# log_path = os.path.join(os.getcwd(),"logs",logFile)
# os.makedirs(log_path,exist_ok=True)

# log_file_path = os.path.join(log_path,logFile)

# logging.basicConfig(
#     filename=log_file_path,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# if __name__=="__main__":
#     logging.info("Logging has started")
import logging
import os
from datetime import datetime

# Create logs directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create a unique log file
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(log_dir, log_file)

# Setup logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Make sure this is NOT overwritten elsewhere
)

# if __name__ == "__main__":
#     logging.info("Logging has started")
