# Onepyece documentation

This documentation is inspired by the offical one : [Documentation API](https://api-onepiece.com/documentation).
Cette documentation est écrite en français car les données de l'API sont en français.
This documentation is written in french because the API data are in french.

## Liste des tous les points d'accès de l'API

Pour voir tous les points d'accès de l'API, référez-vous à la documentation officielle : [Documentation API](https://api-onepiece.com/documentation).
Tous les points d'accès ne sont pas forcément implémentés dans ce package. Par exmple, tous les sous points d'accès "count" sont implicitement implémentés dans les points d'accès principaux. Pour mieux comprendre cela se référer à cet [exemple](examples.py).
Pour voir tous les points d'accès implémentés dans ce package, référez-vous à ce fichier : [functions.py](/onepyece/functions.py) (A noter que ce fichier ne contient que les points d'accès contenant des recherches).

## La classe principale

La classe principale de ce package est la suivante : [interface.py](/onepyece/interface.py)

### Comment l'utiliser ?

Cette classe peut prendre 3 paramètres :

1. Endpoint (obligatoire)
2. Search (facultatif)
3. Resource (facultatif ou obligatoire selon la recherche)

Si vous voulez faire une recherche, vous devez spécifier le paramètre "search" (en plus du paramètre "endpoint" évidemment) et le paramètre "resource" est obligatoire dans la plupart des cas. Si vous voulez récupérer toutes les données d'un point d'accès, vous devez spécifier uniquement le paramètre "endpoint".

### Exemples

<details>
<summary>Toutes les données d'un point d'accès</summary>

```python
import onepyece as op

# Récupérer toutes les données de l'endpoint "films"
films = op.API(endpoint="movies")
print(films)
# Output : 
# Total movies found for this search : 15.
# To see the results, iterate over the object.
```
</details>
<details>
<summary>Recherche avec ressource</summary>

```python
import onepyece as op

# Récupérer tous les personages qui sont des capitaines
# Ici le paramètre resource est le terme de recherche que vous voulez faire. Ainsi on cherche ici les personnages qui ont le job "capitaine"
capitaines = op.API(endpoint="characters", search="job", resource="capitaine")
for capitaine in capitaines:
    print(capitaine.french_name)
# Output :
# Monkey D Luffy
# Cavendish
# Bartolomeo
# ...
```
</details>
<details>
<summary>Recherche sans ressource</summary>

```python
import onepyece as op

# Récupérer tous les équipages de Yonko
yonko = op.API(endpoint="crews", search="yonko")
for yonko in yonko:
    print(yonko.french_name)
# Output :
# L'équipage du Chapeau de Paille
# L'équipage du Roux
# L'équipage des Pirates de Roger
# L'équipage de Barbe Blanche
# L'équipage de Barbe Noire
# L'équipage aux Cent Bêtes
# L'équipage de Big Mom
```
</details>
