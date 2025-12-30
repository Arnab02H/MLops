from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''This Function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name="MLops_Project",
    version="0.1.0",
    author="Arnab Bera",
    packages=find_packages(),
    
    # install_requires=[
    #     "numpy",
    #     "pandas"
    # ]   we can install packages like this but if 
    ## we want the packges automatically come from requirements.txt then we can do like below
    install_requires=get_requirements("requirements.txt"),
)