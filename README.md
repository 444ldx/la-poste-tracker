# Tracker de colis de La Poste en Python

Class Python de suivis de colis à l'aide de l'API de la Poste créé dans le cadre d'un bot Discord de suivis de colis.
La réponse de la fonction **tracker()** ne renvoie pas toute les formations disponible via l'API mais seulement celle que j'ai jugé utile pour mon application. Pour plus d'information voir la documentation de La Poste : https://developer.laposte.fr/products/suivi/2/documentation#heading-0

Remplacer les variables d'environement que j'ai utilisé par les votres ou votre clé OKAPI directement, **déconseillé** !

## Utilisation :

```python
from la_poste.py import Poste

parcel = Poste("PARCEL_ID").tracker()

print(parcel)
```

## Retour

La fonction **tracker()** renvoie un dictionnaire en fontion de la réponse obtenue de l'API
