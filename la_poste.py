import os
from dotenv import load_dotenv
import requests

# replace "config" with the name of your configuration file
# Replace "OKAPI" with your OKAPI key (line 28)
load_dotenv(dotenv_path="config")

class Poste:
    def __init__(self, parcel_id:str, lang:str="fr_FR"):
        self.parcel_id = parcel_id
        self.lang = lang
    
    def url(self):
        """Formatting the request URL

        Returns:
            str: URL
        """
        return "https://api.laposte.fr/suivi/v2/idships/"+ self.parcel_id + "?lang=" + self.lang

    def params(self):
        """Formatting request arguments

        Returns:
            str: Arguments
        """
        return {"Accept": "application/json", "X-Okapi-Key": os.getenv("OKAPI")}

    def tracker(self):
        """Track a parcel

        Returns:
            dict: Parcel informations
        """
        response = requests.get(self.url(), headers=self.params())

        response.encoding = "utf-8"
        json_response = response.json()

        if response.status_code == 200 or response.status_code == 207:

            shipment = json_response.get("shipment")

            return MessageLaPoste({"idShip": shipment.get("idShip", "Numéro introuvable"),
                "product": shipment.get("product", "Produit introuvable"),
                "entryDate": shipment.get("entryDate", "pas encore"),
                "event": shipment.get("event")}).success()
        else:
            idShip = json_response.get("idShip", "Numéro introuvable")
            message = json_response.get("returnMessage", "Erreur")
            return MessageLaPoste({"idShip": idShip,
                "message": message}).error()


if __name__ == "__main__":
    test = Poste("2M04841131282")
    print(test.tracker())