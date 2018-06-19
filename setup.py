from setuptools import setup

from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# TODO: more info

setup(
    name='install-requires',
    version='0.2.0',
    description='Convert requirements between formats',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/orsinium/install-requires',
    author='orsinium',

    packages=['install_requires'],
    extras_require={
        'poetry': ['poetry-setup'],
        'pipfile': ['requirementslib'],
    },
)
