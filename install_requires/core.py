from pathlib import Path

# pip
try:
    # pip>=10
    from pip._internal.download import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.download import PipSession
    from pip.req import parse_requirements

# pipenv
try:
    from requirementslib import Pipfile, Requirement, Lockfile
except ImportError:
    Pipfile = Requirement = Lockfile = None

# poetry
try:
    from poetry_setup import PoetrySetup
except ImportError:
    PoetrySetup = None


VCS_LIST = ('git+', 'svn+', 'hg+', 'bzr+')
SCHEME_LIST = ('http://', 'https://', 'ftp://', 'ftps://', 'file://')


class Setup:
    def __init__(self, path):
        if isinstance(path, str):
            path = Path(path)
        self.path = path

    @staticmethod
    def _parse_requirements(reqs):
        install_requires = []
        dependency_links = []
        for req in reqs:
            if req.startswith('-i'):
                continue
            if req.startswith('-e'):
                req = req[2:]
            req = req.strip()
            if any(req.startswith(vcs) for vcs in VCS_LIST):
                dependency_links.append(req)
            elif any(req.startswith(sch) for sch in SCHEME_LIST):
                dependency_links.append(req)
            else:
                install_requires.append(req)
        return install_requires, dependency_links

    def from_requirements(self):
        path = self.path / 'requirements.txt'
        requirements = parse_requirements(str(path), session=PipSession())
        requirements = [str(r.req) for r in requirements]
        return self._parse_requirements(requirements)

    def from_pipfile(self):
        if Pipfile is None:
            raise ImportError('please, install extra requirements: install-requires[pipfile]')

        project = Pipfile.load(self.path)
        requirements = []
        packages = project.get_sections()['packages'].items()
        for name, version in packages:
            req = Requirement.from_pipfile(name, version)
            requirements.append(req.as_line())
        return self._parse_requirements(requirements)

    def from_lockfile(self):
        if Pipfile is None:
            raise ImportError('please, install extra requirements: install-requires[pipfile]')

        lockfile = Lockfile.create(self.path)
        requirements = lockfile.as_requirements(dev=False)
        return self._parse_requirements(requirements)

    def from_poetry(self):
        if PoetrySetup is None:
            raise ImportError('please, install extra requirements: install-requires[poetry]')

        ps = PoetrySetup(self.path)
        requirements = ps.get_requirements().split('\n')
        return self._parse_requirements(requirements)


class Requirements(Setup):
    @staticmethod
    def _parse_requirements(reqs):
        return reqs


DUMPERS = {
    'setup.py': Setup,
    'requirements.txt': Requirements,
}
LOADERS = {
    'requirements.txt': 'from_requirements',
    'Pipfile': 'from_pipfile',
    'Pipfile.lock': 'from_lockfile',
    'pyproject.toml': 'from_poetry',
}


def convert(name_from, name_to, path='.'):
    loader = LOADERS[name_from]
    dumper = DUMPERS[name_to]
    return getattr(dumper(path), loader)()
