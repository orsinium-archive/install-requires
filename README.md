# install_requires

## requirements.txt -> setup.py

See [requirements2setup](requirements2setup/setup.py) example.

## Pipfile -> setup.py

See [pipfile2setup](pipfile2setup/setup.py) example.


## Pipfile.lock -> setup.py

See [lockfile2setup](lockfile2setup/setup.py) example.


## pyproject.toml -> setup.py, requirements.txt

See [poetry-setup](https://github.com/orsinium/poetry-setup) project.

# requirements.txt -> Pipfile

```bash
pipenv install --requirements requirements.txt
```

## Pipfile.lock -> Pipfile

```bash
pipenv lock
```

## Pipfile.lock -> requirements.txt

```bash
pipenv lock --requirements > requirements.txt
```
