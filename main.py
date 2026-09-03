from utils.logger import setupLogger
from api.cityDataFetch import CityDataFetch
from api.weatherDataFetch import WeatherDataFetch
from  Data.models.data_model import CityData
from utils.formatters import city_formatter,weather_formatter

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

    weather_fetch = WeatherDataFetch(city_data)
    weather_data = weather_fetch.fetchWeather()
    if not name:
        print("-----------Default----------")
    city_formatter(city_data)
    weather_formatter(weather_data)


if __name__ == "__main__":
    main()