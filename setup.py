from setuptools import setup
from typing import List   


# Declaring variables for setup functions
PROJECT_NAME = "forest_cover_type"
PROJECT_VERSION = "0.0.1"
PROJECT_AUTHOR = "atchayapraba"
PROJECT_DESCRIPTION = """
This is my first internship project at ineuron. It predicts the forest cover type. 
"""
PACKAGES = ["forestcovertype"]
REQUIREMWNTS_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """
    Description: This function returns the list of requirements (name of libraries required to be installed) 
    as mentioned in the 'rerequirements.txt' file.

    return: List containg str
    """
    with open(REQUIREMWNTS_FILE_NAME, "r+") as requirements_file:
        return requirements_file.readline()


setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    author=PROJECT_AUTHOR,
    description=PROJECT_DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirements_list()
)
