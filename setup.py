from setuptools import find_packages,setup

setup(
    name= 'mlproject',
    version= '0.0.1',
    author= 'dengveng',
    author_email= 'dengveng69@gmail.com',
    packages= find_packages(),
    install_requires= ['numpy', 'pandas'],
)