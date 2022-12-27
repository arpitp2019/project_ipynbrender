import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s):%(levelname)s]:%(message)s")

while True:
    project_name=input("enter the project name ")
    if project_name ! = '':
        break

logging.info(f"project name is {project_name}")

