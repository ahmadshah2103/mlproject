from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path) -> List[str]:
    '''
    Parameters: 
        file_path (str):    path to the file we want to extract requirements from.
    Returns:
        requirements (list):    list of all the requirements.
    '''
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Ahmad Shah',
    author_email='ahmad1911491@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
