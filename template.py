import os
from pathlib import Path
import logging

project_name = "datascience"

list_of_files = [
    ".github/workflows/.gitkeep", ## helps in deploying the workflow
    f"src/{project_name}/__init__.py", ## helps in making the project a package
    f"src/{project_name}/components/__init__.py", #For holding all the components such as data ingestion, data preprocessing, model training, model evaluation
    f"src/{project_name}/utils/__init__.py", #For holding all the utility(generic) functions
    f"src/{project_name}/utils/common.py", ## Files which are common to all the components
    f"src/{project_name}/config.py/__init__.py", ## For holding all the configuration files
    f"src/{project_name}/config.py/configuration.py", ## For holding all the configuration files
    f"src/{project_name}/pipeline/__init__.py", ## For holding all the pipeline files
    f"src/{project_name}/entity/__init__.py",  ## For holding all the entities
    f"src/{project_name}/entity/config_entity.py", ## For holding all the entities
    f"src/{project_name}/constants/__init__.py", ## For holding all the constants
    "config/config.yml", ## For holding all the configuration files
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    ".gitignore",
    ".dockerignore",
    "README.md",
    "LICENSE",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py",
]

def create_files():
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        if filedir and not os.path.exists(filedir):
            os.makedirs(filedir)
            logging.info(f"Created directory: {filedir}")
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                f.write("")
                logging.info(f"Created Empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")


if __name__ == "__main__":
    create_files()
