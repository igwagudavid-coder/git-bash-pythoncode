from dataclasses import dataclass

@dataclass
class CityData:
    name: str
    population: int
    longitude: float
    latitude: float



@dataclass
class WeatherData:
    time :str
    temperature :float
    relative_humidity :float
    wind_speed :float
    weather_status: str
    is_day: str