import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
    "requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    # Create directory if needed
    if filedir != Path(""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Convert filepath to string before checking
    if (not os.path.exists(str(filepath))) or (os.path.getsize(str(filepath)) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
