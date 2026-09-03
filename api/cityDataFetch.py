import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from Data.models.data_model import CityData
from config.app_config import BASE_DIR
import json

class CityDataFetch:
    def __init__(self,name:str=""):
        self.name = name.strip()
        self.BASE_DIR = BASE_DIR
        with open(f'{BASE_DIR}/config/config.json') as file:
            self.config= json.load(file)["lat_config"]
        self.base_url = self.config["url"]
        self.url = None
        self.default_name = self.config["default_name"]


    def build_url(self):

        self.url = self.base_url.replace("{city_name}", self.name) if self.name else self.base_url.replace("{city_name}", self.default_name)

    def fetchData(self):
        self.build_url()
        while True:
            try:
                response = requests.get(url =self.url, timeout = 30)
                response.raise_for_status()
                data = response.json()
                break
            except ConnectionError as e:
                print(f"Couldn't connect to {self.url}, check your internet connection and try again.")
                again = input("Try again? (y/n): ").strip().lower()
                if again != "y":
                    raise ConnectionError("Couldn't connect the weather service (bad internet connection).{City Data Fetch}")
            except Timeout as e:
                print("Web connection timed out.")
                raise ConnectionError("Connection timed out {City Data Fetch}")
            except HTTPError as e:
                print(f"Bad server response {response.status_code}. {e}")
                raise ConnectionError(f"Bad server response {response.status_code}. {e} City Data Fetch")

        self.name = data["results"][0]["name"]
        longitude = data["results"][0]["longitude"]
        latitude = data["results"][0]["latitude"]
        population = data["results"][0]["population"]
        return CityData(
            name = self.name,
            population = population,
            longitude = longitude,
            latitude = latitude )



