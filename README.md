# One Pyece
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/onepyece)
![PyPI](https://img.shields.io/pypi/v/onepyece)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/icepick4/onepyece/python-package.yml)
![PyPI - License](https://img.shields.io/pypi/l/onepyece)
![GitHub last commit](https://img.shields.io/github/last-commit/icepick4/onepyece)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Python API wrapper for https://api-onepiece.com/ \
Thank's to this package you can simply get informations about One Piece characters, fruits, crews, etc.
Learn more about possibilities in the [Usage](#usage) section.
This package is still in development and it's my very first python package, so it may not be stable.

## Installation

There are several solutions :

- Use this command ``pip install onepyece`` to get it from [PyPi](https://pypi.org/project/onepyece/)
- Use this command ``pip install git+https://github.com/icepick4/onepyece`` to download it from this repo.
- Download either the .zip or the tar.gz archive from the last release and then use this command `` pip install <path_to_archive> ``

## Usage

```py
>>> import onepyece as op
>>> sanji = op.character_by_name('sanji') # You can get a character by its name
>>> sanji.birthday
'2000-03-02'
>>> nb_fruits = op.count_fruits() # You can get the count of a specific endpoint
>>> nb_fruits.count
197
>>> nb_fruits.url
https://api.api-onepiece.com/fruits/count
>>> crews = op.API('crews') # List of all the crews in dict form as you can see below
>>> crews.results[0]
{'id': 1, 'french_name': 'L’équipage du Chapeau de Paille', 'roman_name': 'Mugiwara no Ichimi', 'description': '', 'total_prime': 
'3.161.000.100', 'number': '10', 'status': 'actif', 'isYonko': True, 'affiliation': ''}
>>> crews.count # You can implicitly get the count of an endpoint by getting the whole list of it.
149
```

To get more basics functions visit that [file](onepyece/functions.py) which contains them, otherwise you can simply create API objects.

## Tests

You can test the application by running ``python -m tests``



