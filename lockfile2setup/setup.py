from setuptools import setup, find_packages
from pathlib import Path
from pip._internal import main as pip


pip(['install', 'requirementslib'])


from requirementslib import Lockfile  # noQA


path = Path(__file__).parent
lockfile = Lockfile.create(path)


setup(
    name='package-name',
    version='0.1.0',
    description='Description also required',
    packages=find_packages(),
    install_requires=lockfile.as_requirements(dev=False),
)
