# openxlab with Python 3.1.12 support

This repo is a fork of [openxlab](https://pypi.org/project/openxlab/).

The source files are unchanged except for:

- Adding a pyproject.toml file
- Relaxing Python version requirements

## Install

```sh
# If you have the existing openxlab, you may need to unistall it
pip uninstall openxlab
pip install openxlab@git+https://github.com/Presence-AI/openxlab.git#egg=openxlab
```

If you use requirements.txt, use the following:

```requirements
openxlab @ git+https://github.com/Presence-AI/openxlab.git#egg=openxlab
```

## Development

### virtualenv

openxlab has a types module, which shadows Python's types module.
To get around this:

```sh
mkdir .venv
cd .venv
python -m venv .
```

### requirements-dev.txt

The upstream version of openxlab & pip-check-updates is in requirements-dev.txt.
This allows inspection & copying of the upstream source into this project.

#### Check for updates to the upstream openxlab

```sh
.venv/bin/pcu ./requirements-dev.txt
```

#### Sync upstream openlab source code

```sh
rsync -avh .venv/lib/python3.12/site-packages/openxlab/* ./ --delete
```
