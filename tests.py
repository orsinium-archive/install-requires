from pathlib import Path
from install_requires import convert


def test_working():
    path = Path('./example')
    assert 'deal' in convert('Pipfile', 'setup.py', path)[0]
    assert 'deal' in convert('Pipfile.lock', 'setup.py', path)[0][0]
    assert 'deal==2.1.0' in convert('requirements.txt', 'setup.py', path)[0]
