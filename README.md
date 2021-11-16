# Tracker de colis de La Poste en Python

Class Python de suivis de colis à l'aide de l'API de la Poste créé dans le cadre d'un bot Discord de suivis de colis.
La réponse de la fonction **tracker()** ne renvoie pas toute les formations disponible via l'API mais seulement celle que j'ai jugé utile pour mon application. Pour plus d'information voir la documentation de La Poste : https://developer.laposte.fr/products/suivi/2/documentation#heading-0

Remplacer les variables d'environement que j'ai utilisé par les votres ou votre clé OKAPI directement, **déconseillé** !

## Utilisation :

Seul la fontion **tracker()** est utilisable, les autres fontion servent à apporté des information à celle-ci.

```python
from la_poste.py import Poste

parcel = Poste("PARCEL_ID").tracker()
```

## Retour

La fonction **tracker()** renvoie un dictionnaire en fontion de la réponse obtenue de l'API.

**En cas de réponse 200 :** 
```python
return {"idShip": shipment.get("idShip", "Numéro introuvable"),
        "product": shipment.get("product", "Produit introuvable"),
        "entryDate": shipment.get("entryDate", "pas encore"),
        "event": shipment.get("event")}
```

**En cas d'erreur :** 
```python
return {"idShip": json_response.get("idShip", "Numéro introuvable"),
        "message": json_response.get("returnMessage", "Erreur")}
```
## Retourner l'ensemble de la requête

Pour retouner l'ensemble des informations vous pouvez remplacer :

```python
if response.status_code == 200 or response.status_code == 207:
            
  shipment = json_response.get("shipment")
            
  return {"idShip": shipment.get("idShip", "Numéro introuvable"),
          "product": shipment.get("product", "Produit introuvable"),
          "entryDate": shipment.get("entryDate", "pas encore"),
          "event": shipment.get("event")}

else:
  return {"idShip": json_response.get("idShip", "Numéro introuvable"),
          "message": json_response.get("returnMessage", "Erreur")}
```

Par :

```python
return json_response
```
