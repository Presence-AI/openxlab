# openxlab with Python 3.1.12 support

This repo is a fork of [openxlab](https://pypi.org/project/openxlab/).

The source files are unchanged except for:

- Adding a pyproject.toml file
- Relaxing Python version requirements

## Install

```
# If you have the existing openxlab, you may need to unistall it
pip uninstall openxlab
pip install openxlab@git+https://github.com/Presence-AI/openxlab.git#egg=openxlab
```

If you use requirements.txt, use the following:

```
openxlab @ git+https://github.com/Presence-AI/openxlab.git#egg=openxlab
```
