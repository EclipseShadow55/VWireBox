import twitchAPI
import misc
import requests
import os
from datetime import datetime


if __name__ == "__main__":
    # Create new log file
    with open(f"{datetime.now().strftime('%d/%m/%Y_%H:%M:%S.%f')}.txt", "x") as f:
        f.write("")
    # Load user data
