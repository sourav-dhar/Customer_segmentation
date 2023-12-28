import os,sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"config/config.yaml",
    f"config/schema.yaml",
    "schema.yaml",
    "params.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "logs.py",
    "exception.py",
    "requirements.txt",
    "dvc.yaml",
    "Dockerfile",
    "templates/index.html",
    "research/trials.ipynb"   
]

#split into folders and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating direcoty- {filedir} for the file- {filename}")
        
    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty folders in- {filepath}")
    else:
        logging.info(f"file is already present in- {filepath}")