from setuptools import setup, find_packages
from pathlib import Path
from pip._internal import main as pip


pip(['install', 'requirementslib'])


from requirementslib import Pipfile, Requirement # noQA


path = Path(__file__).parent
project = Pipfile.load(path)
requirements = []
for name, version in project.get_sections()['packages'].items():
    req = Requirement.from_pipfile(name, version)
    requirements.append(req.as_line().strip())


setup(
    name='package-name',
    version='0.1.0',
    description='Description also required',
    packages=find_packages(),
    install_requires=requirements,
)
