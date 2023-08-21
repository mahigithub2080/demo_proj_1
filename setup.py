from setuptools import find_packages,setup
from typing import List

HYPHON_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of elements

    """
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
            
    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author='mahi_patil',
    author_email='mahipatil1593@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)