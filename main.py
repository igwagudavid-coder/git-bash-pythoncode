from utils.logger import setupLogger
from api.cityDataFetch import CityDataFetch
from api.weatherDataFetch import WeatherDataFetch
from  Data.models.data_model import CityData
from utils.formatters import city_formatter,weather_formatter
import time
from requests.exceptions import Timeout,HTTPError,ConnectionError

def weatherMonitor( weather_data, weather_fetch, logger, interval = 120):
    last_weather=weather_data
    while True:
        try:
            weather_data = weather_fetch.fetchWeather()

        except (ConnectionError, Timeout ,HTTPError) as e:
            logger.error(str(e))
            time.sleep(30)
            continue

        if weather_data != last_weather:
            weather_formatter(weather_data)
            last_weather = weather_data

        time.sleep(interval)



def main():
    name = input("What city would you like data on?(Leave blank for default): ").strip().lower()
    logger = setupLogger()


    city_fetch = CityDataFetch(name)

    try:
        city_data  = city_fetch.fetchData()
    except Exception as e:
        print(f"Data fetching failed: {e}")
        logger.error(str(e))
        exit()

    logger.info("System Started successfully!")

    try:
        weather_fetch = WeatherDataFetch(city_data)
    except Exception as e:
        print(f"Weather Fetching failed: {e}")
        logger.error(str(e))
        exit()
    weather_data = weather_fetch.fetchWeather()
    if not name:
        print("-----------Default----------")
    #city_formatter(city_data)
    weather_formatter(weather_data)
    weatherMonitor(weather_data,weather_fetch, logger)

if __name__ == "__main__":
    main()