# Importing libraries
import os
import setuptools
from dotenv import load_dotenv
from typing import List

'''
    This script is the configuration file or setup of our project.
    It contains all the major information related to our project such as 
    a) version number / user name / project name.
    This information is useful while uploading this project as a PyPi package.
'''


# Loading the enviornment variables
load_dotenv()
SRC_REPO = os.environ['SRC_REPO']
VERSION = os.environ['__version__']
AUTHOR_NAME = os.environ['AUTHOR_USER_NAME']
AUTHOR_EMAIL = os.environ['AUTHOR_EMAIL']
REPO_NAME = os.environ['REPO_NAME']

# Reading the README.md file and saving it's contents as long_description for 
# our python package
def get_readme(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        long_description = f.read()

        return long_description



# Fetch requirements.txt file
def get_requirements(file_path:str) -> List[str]:
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]

        if "-e ." in lines:
            lines.remove("-e .")

        return lines



# Project Configuration
# reference link : https://pythonhosted.org/an_example_pypi_project/setuptools.html
setuptools.setup(
    name=SRC_REPO,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Music Genre Classification",
    long_description=get_readme("README.md"),
    packages=setuptools.find_packages(),
    install_requires=get_requirements("requirements.txt"),
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/"
)