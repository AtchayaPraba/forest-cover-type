from setuptools import setup, find_packages
from typing import List   


# Declaring variables for setup functions
PROJECT_NAME = "forest_cover_type"
PROJECT_VERSION = "0.0.1"
PROJECT_AUTHOR = "atchayapraba"
PROJECT_DESCRIPTION = """
This is my first internship project at ineuron. It predicts the forest cover type. 
"""
REQUIREMWNTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function returns the list of requirements (name of libraries required to be installed) 
    as mentioned in the 'rerequirements.txt' file.

    return: List containg str
    """
    with open(REQUIREMWNTS_FILE_NAME, "r+") as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list = requirements_list.remove(HYPHEN_E_DOT)
        else:
            pass
        return requirements_list

setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    author=PROJECT_AUTHOR,
    description=PROJECT_DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
)
