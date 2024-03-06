import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.mow().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.cwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOGS_FILE_PATH=OS.PATH.JOIN(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[ %(astime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)
