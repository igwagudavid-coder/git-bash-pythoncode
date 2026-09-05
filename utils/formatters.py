from Data.models.data_model import CityData,WeatherData


def city_formatter(city_data:CityData):
    print("\n\n--------City data--------\n")
    print(f"Name: {city_data.name}")
    print(f"Population: {city_data.population}")
    print(f"Latitude: {city_data.latitude}")
    print(f"Longitude: {city_data.longitude}")


def weather_formatter(weather_data:WeatherData):
    print("\n\n--------Weather data--------\n")
    print(f"Time: {weather_data.time}")
    print(f"Temperature: {weather_data.temperature}")
    print(f"Relative Humidity: {weather_data.relative_humidity}")
    print(f"Wind Speed: {weather_data.wind_speed}")
    print(f"Weather Status: {WEATHER_CODES.get(weather_data.weather_status, "unknown")}")
    print(f"Is day? : {weather_data.is_day}")



WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}