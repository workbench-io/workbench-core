# workbench-core

[![CI](https://github.com/workbench-io/workbench-core/workflows/CI/badge.svg)](https://github.com/workbench-io/workbench-core/actions)
[![Documentation Status](https://readthedocs.org/projects/workbench_core/badge/?version=latest)](https://workbench_core.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/workbench_core)](https://pypi.org/project/workbench_core)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/workbench_core)](https://pypi.org/project/workbench_core)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Workbench core concepts and classes.

- Documentation: https://workbench-core.readthedocs.io

## Installation

Install the latest version from PyPI:

```
pip install workbench_core
```
## Development setup

After cloning the repository, you can easily install the development environment and tools
([black](https://github.com/psf/black), [pylint](https://www.pylint.org), [mypy](http://mypy-lang.org), [pytest](https://pytest.org), [tox](https://tox.readthedocs.io))
with:

```
git clone https://github.com/workbench-io/workbench-core.git
cd workbench_core
pip install -e .[dev]
```

And run the checks & tests with tox:

```
tox
```

The documentation is built with [sphinx](https://www.sphinx-doc.org):

```
cd docs

# Windows
.\make.bat clean
.\make.bat html

# Linux
make clean html
```
