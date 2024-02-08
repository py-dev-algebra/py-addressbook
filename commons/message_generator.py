from datetime import datetime as dt
from commons.app_constants import (LOG_INFO,
                                   LOG_WARNING,
                                   LOG_ERROR)

def generate_message(text: str):
    pass

def generate_log_message(text: str, log_type: str = LOG_INFO):
    return f'{log_type} - {dt.now().strftime("%Y-%m-%d %H:%M:%S")} - {text}\n'
  # ERROR - 2024-02-08 19:20 - Dogodila se greska error type ...
  # INFO - 2024-02-08 19:20 - Dogodila se greska error type ...