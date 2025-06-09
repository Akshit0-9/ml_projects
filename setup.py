from setuptools import find_packages,setup
from typing import List

# below function returns list of requirements.
Hyphen_edot = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n"," ")for req in requirements]
        
        if Hyphen_edot in requirements:
            requirements.remove(Hyphen_edot)
            
    return requirements


setup(
name= 'ML-Project',
version= '0.0.1',
author= 'Akshit',
author_email= 'akshit.shar009@gmail.com',
packages = find_packages(),
libraries_install = get_requirements('requirements.txt')
)