import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s):%(levelname)s]:%(message)s")

while True:
    project_name=input("enter the project name ")
    if project_name != '':
        break

logging.info(f"project name is {project_name}")
list_of_files=['.github/workflows/.gitkeep', 
               f"src/{project_name}__init.py__",
               f"tests/__init__.py",
               f"tests/unit/__init__.py",
               f"tests/integration/__init__.py"
               "init_setup.sh",
               "requirements.txt",
               "requirements_dev.txt",
               "setup.py",
               "pyproject.toml",
               "setup.tcfg",
               "tox.ini"
               ]

for i in list_of_files:
    i = Path(i)
    filedir, filename = os.path.split(i)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(i)) or (os.path.getsize(i) == 0):
        with open(i, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {i}")
    else:
        logging.info(f"file is already present at: {i}")
        



