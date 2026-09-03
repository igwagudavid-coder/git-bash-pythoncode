from Data.models.data_model import CityData,WeatherData


def city_formatter(city_data:CityData):
    print("\n\n--------City data--------\n")
    print(f"Name: {city_data.name}")
    print(f"Population: {city_data.population}")
    print(f"Latitude: {city_data.latitude}")
    print(f"Longitude: {city_data.longitude}")


def weather_formatter(weather_data:WeatherData):
    print("\n\n--------Weather data--------\n")
    #print(f"Time: {weather_data.time}")
    print(f"Temperature: {weather_data.temperature}")
    print(f"Relative Humidity: {weather_data.relative_humidity}")
    print(f"Wind Speed: {weather_data.wind_speed}")
    print(f"Weather Status: {weather_data.weather_status}")
    print(f"Is day? : {weather_data.is_day}")
