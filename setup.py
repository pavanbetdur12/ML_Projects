from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    
    """Reads the requirements from a file and returns them as a list."""
    
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements       
setup(
name='mlproject',
version='0.1.0',
author='Pavan',
author_email='pavanbetdur12@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
description='A machine learning project setup',  

)