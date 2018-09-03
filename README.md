# install_requires

Convert between dependency describing formats.

Input formats:
* `Pipfile`
* `Pipfile.lock`
* `pyproject.toml` (poetry)
* `requirements.txt`

Output formats:
* `setup.py` (return `install_requires` and `dependency_links`)
* `requirements.txt` (return list of lines)

## Install

Install with needed extra requirements:

```bash
pip install install-requires[pipfile]
pip install install-requires[poetry]
```

Or from your setup.py:

```python
from pip._internal import main as pip

pip(['install', 'install-requires[pipfile]'])
pip(['install', 'install-requires[poetry]'])
```

## CLI usage

```bash
install-requires example/Pipfile requirements.txt
```

Available conversions:

1. Pipfile -> requirements.txt
1. Pipfile.lock -> requirements.txt
1. pyproject.toml -> requirements.txt

## API usage

Pass input format, output format and path to file that must be parsed into `convert` function:

```python
from pathlib import Path
from install_requires import convert

path = Path(__file__).parent
convert('pyproject.toml', 'setup.py', path)
```

Available conversions:

1. Pipfile -> requirements.txt
1. Pipfile.lock -> requirements.txt
1. pyproject.toml -> requirements.txt
1. Pipfile -> setup.py
1. Pipfile.lock -> setup.py
1. pyproject.toml -> setup.py
1. requirements.txt -> setup.py

See [example](example/setup.py) for more details.
