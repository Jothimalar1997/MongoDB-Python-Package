from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.1"
REPO_NAME = "MongoDB Python Package"
PKG_NAME= "databaseautomation"
AUTHOR_USER_NAME = "Jothimalar Paulpandi"
AUTHOR_EMAIL = "reachtojothi@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/Jothimalar1997/MongoDB-Python-Package",
    project_urls={
        "Bug Tracker": "https://github.com/Jothimalar1997/MongoDB-Python-Package/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )