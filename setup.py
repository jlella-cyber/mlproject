from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements

    if HYPEN_E_DOT in requirements:
         requirements.remove (HYPEN_E_DOT)


setup(
    name="mlproject",
    version="0.0.1",
    author="Jahnavi Lella",
    author_email="majadevops2025@gmail.com",
    packages=find_packages(),
    install_requires=[ 'pandas', 'numpy', 'matplotlib', 'scikit-learn', 'seaborn', 'statsmodels'
    ],
)