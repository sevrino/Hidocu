import logging
from datetime import datetime

def log():
    date = datetime.today().strftime("%Y/%m/%d-%H:%M:%S")
    logging.basicConfig(filename = f"log/app.log", level = logging.DEBUG)