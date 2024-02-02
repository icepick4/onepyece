# Onepyece Documentation

This documentation is inspired by the API documentation used by Onepyece: [API Documentation](https://api-onepiece.com/documentation).

Voir [version française](/docs/README.fr.md)

## List of All API Endpoints

To see all the API endpoints, refer to the official documentation: \[API Documentation\]\(https://api-onepiece.com/documentation\).
Not all endpoints are necessarily implemented in this package. For example, all "count" sub-endpoints are implicitly implemented in the main endpoints. For a better understanding, refer to this [exemple](examples.py).
To see all the endpoints implemented in this package, refer to this file: `functions.py` (Note that this file only contains endpoints involving searches).

## The Main Class

The main class of this package is located in `interface.py`.

### How to Use It?

This class can take 3 parameters:

1. `Endpoint` (mandatory)
2. `Search` (optional)
3. `Language` (optional, default is English (`lang="en"`))
4. `Resource` (optional or mandatory depending on the search)

If you want to perform a search, you must specify the "search" parameter (in addition to the "endpoint" parameter, obviously), and the "resource" parameter is mandatory in most cases. If you want to retrieve all the data from an endpoint, you only need to specify the "endpoint" parameter. Two languages are available: French and English, by default English will be used, otherwise change the `lang` parameter in the class.

### Examples

#### All Data from an Endpoint

To retrieve all data from the "movies" endpoint in French:
```python
import onepyece as op

movies = op.API(endpoint="movies", lang="fr")
print(movies)
# Output: 
# Total movies found for this search: 15.
# To see the results, iterate over the object.
```

#### Search with Resource

To retrieve all characters who are captains in English:
```python
import onepyece as op

captains = op.API(endpoint="characters", search="job", resource="captain", lang="en")
for captain in captains:
    print(captain.french_name)
# Output:
# Monkey D Luffy
# Cavendish
# Bartolomeo
# ...
```

#### Search without Resource

To retrieve all Yonko crews in French:
```python
import onepyece as op

yonkos = op.API(endpoint="crews", search="yonko", lang="fr")
for yonko in yonkos:
    print(yonko.french_name)
# Output:
# The Straw Hat Crew
# The Red Hair Crew
# The Roger Pirates
# The Whitebeard Pirates
# The Blackbeard Pirates
# The Beasts Pirates
# The Big Mom Pirates
```
