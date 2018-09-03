import sys
from pathlib import Path
from .core import convert as _convert


def convert(path_from=sys.argv[-2], path_to=sys.argv[-1]):
    # name_from and input path
    path_from = Path(path_from)
    if path_from.stem in ('Pipfile', 'pyproject.toml'):
        name_from = path_from.stem
        path = path_from.parent
    else:
        name_from = 'requirements.txt'
        path = path_from

    # name_to and output path
    path_to = Path(path_to)
    name_to = 'requirements.txt'

    # convert
    result = _convert(name_from, name_to, path)

    # save
    with path_to.open('w') as stream:
        stream.write('\n'.join(result))
