# Documentation Onepyece

Cette documentation est inspirée de la documentation de l'API utilisée par Onepyece : [Documentation API](https://api-onepiece.com/documentation).

See [english version](/docs/README.en.md)

## Liste de tous les points d'accès de l'API

Pour voir tous les points d'accès de l'API, référez-vous à la documentation officielle : [Documentation API](https://api-onepiece.com/documentation).
Tous les points d'accès ne sont pas forcément implémentés dans ce package. Par exemple, tous les sous-points d'accès "count" sont implicitement implémentés dans les points d'accès principaux. Pour mieux comprendre, référez-vous à cet [exemple](examples.py).
Pour voir tous les points d'accès implémentés dans ce package, référez-vous à ce fichier : `functions.py` (Notez que ce fichier contient uniquement les points d'accès impliquant des recherches).

## La classe principale

La classe principale de ce package se trouve dans `interface.py`.

### Comment l'utiliser ?

Cette classe peut prendre 3 paramètres :

1. `Endpoint` (obligatoire)
2. `Search` (facultatif)
3. `Language` (facultatif, anglais par défaut (`lang="en"`))
4. `Resource` (facultatif ou obligatoire selon la recherche)

Si vous souhaitez effectuer une recherche, vous devez spécifier le paramètre "search" (en plus du paramètre "endpoint", évidemment), et le paramètre "resource" est obligatoire dans la plupart des cas. Si vous souhaitez récupérer toutes les données d'un point d'accès, vous devez spécifier uniquement le paramètre "endpoint". Deux langues sont disponibles : français et anglais, par défaut l'anglais sera utilisé, sinon changez le paramètre `lang` dans la classe.

### Exemples

#### Toutes les données d'un point d'accès

Pour récupérer toutes les données du point d'accès "movies" en français :
```python
import onepyece as op

movies = op.API(endpoint="movies", lang="fr")
print(movies)
# Sortie : 
# Total de films trouvés pour cette recherche : 15.
# Pour voir les résultats, itérez sur l'objet.
```

#### Recherche avec ressource

Pour récupérer tous les personnages qui sont capitaines en anglais :
```python
import onepyece as op

captains = op.API(endpoint="characters", search="job", resource="captain", lang="en")
for captain in captains:
    print(captain.french_name)
# Sortie :
# Monkey D Luffy
# Cavendish
# Bartolomeo
# ...
```

#### Recherche sans ressource

Pour récupérer tous les équipages de Yonko en français :
```python
import onepyece as op

yonkos = op.API(endpoint="crews", search="yonko", lang="fr")
for yonko in yonkos:
    print(yonko.french_name)
# Sortie :
# L'équipage du Chapeau de Paille
# L'équipage du Roux
# L'équipage des Pirates de Roger
# L'équipage de Barbe Blanche
# L'équipage de Barbe Noire
# L'équipage aux Cent Bêtes
# L'équipage de Big Mom
```
