from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="student",
    version='0.0.1',
    author='Aman007rj',
    author_email='aman007rj@gmail.com',
    packages=find_packages(),
        url='https://github.com/Aman007rj/student',
        description='A package for student management',
        install_requires=get_requirements('requirements.txt'),
)