# One Pyece
Python package for https://api-onepiece.com/ 

## Installation

There are several solutions :

- Use this command ``pip install git+https://github.com/icepick4/one-pyece`` to download it from this repo.
- [⚠️COMING SOON] Download either the .zip or the tar.gz archive from the last release and then use this command `` pip install <path_to_archive> ``

## Usage

```py
>>> import onepyece as op
>>> sanji = op.character_by_name('sanji') 
>>> sanji.birthday
'2000-03-02'
>>> nb_fruits = op.count_fruits()
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



