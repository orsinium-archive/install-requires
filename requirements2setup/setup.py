from setuptools import setup, find_packages
from pathlib import Path


try:
    # pip>=10
    from pip._internal.download import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.download import PipSession
    from pip.req import parse_requirements


path = Path(__file__).parent / 'requirements.txt'
requirements = parse_requirements(path, session=PipSession())
requirements = [str(r.req) for r in requirements]


setup(
    name='package-name',
    version='0.1.0',
    description='Description also required',
    packages=find_packages(),
    install_requires=requirements,
)
