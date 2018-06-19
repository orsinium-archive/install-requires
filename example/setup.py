from setuptools import setup, find_packages
from pathlib import Path
from pip._internal import main as pip


pip(['install', 'install-requires[pipfile]'])


from install_requires import convert  # noQA


path = Path(__file__).parent
install_requires, dependency_links = convert('Pipfile', 'setup.py', path)

setup(
    name='package-name',
    version='0.1.0',
    description='Description also required',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dependency_links,
)
