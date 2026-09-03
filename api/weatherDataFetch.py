import requests
from Data.models.data_model import CityData,WeatherData
from config.app_config import BASE_DIR
import json


class WeatherDataFetch():
    def __init__(self,city_data:CityData):
        self.BASE_DIR = BASE_DIR
        self.url = None
        with open(f'{BASE_DIR}/config/config.json') as file:
            self.config =json.load(file)["weather_config"]
        self.params = None
        self.longitude = city_data.longitude
        self.latitude = city_data.latitude


    def buildParams(self):
        params = self.config["params"]
        params["longitude"] = self.longitude
        params["latitude"] = self.latitude
        self.params = params

    def buildUrl(self):
            url = self.config["url"]
            self.url = url

    def fetchWeather(self):
        self.buildParams()
        self.buildUrl()

        response = requests.get(url = self.url, params = self.params, timeout = 20)
        data = response.json()

        time = data["current"]["time"]
        temp = data["current"]["temperature_2m"]
        rel_h = data["current"]["relative_humidity_2m"]
        wind_speed = data["current"]["wind_speed_10m"]
        weather_status = data["current"]["weather_code"]
        is_day ="yh" if  data["current"]["is_day"] == 1 else "nh"
        return WeatherData(
            time = time,
            temperature= temp,
            relative_humidity= rel_h,
            wind_speed= wind_speed,
            weather_status = weather_status,
            is_day = is_day
        )




