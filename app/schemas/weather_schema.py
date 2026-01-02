"""
# Weather Schema

This library (`app/schemas/weather_schema.py`) describes the information
returned by the [WeatherAPI](https://www.weatherapi.com/docs/#weather-icons)
API, as used by the [weather](weather.md) library.

The top level responses used are [Current_Weather](#Current_Weather) and
[Forecast_Weather](#Forecast_Weather)
"""
from typing import List

from pydantic import BaseModel


class Location(BaseModel):
    """
    Location as matched by Weather API to the location name given

    Args:
        name (str): e.g. "Melbourne"
        region (str): e.g. "Victoria"
        country (str): e.g. "Australia"
        lat (float): e.g. -37.8167
        lon (float): e.g. 144.9667
        tz_id (str): e.g. "Australia/Melbourne"
        localtime_epoch (int): e.g. 1767329771
        localtime (str): e.g. "2026-01-02 15:56"
    """

    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str


class Condition(BaseModel):
    """
    Weather Conditions at the location, as returned by Weather API

    Args:
        text (str): e.g. "Sunny"
        icon (str): e.g. "//cdn.weatherapi.com/weather/64x64/day/113.png"
        code (int): e.g. 1000
    """

    text: str
    icon: str
    code: int


class Current(BaseModel):
    """
    Current weather (including 'Condition') at the location, as returned by Weather API

    Args:
        last_updated_epoch (int): e.g. 1767329100
        last_updated (str): e.g. "2026-01-02 15:45"
        temp_c (float): e.g. 26.1
        temp_f (float): e.g. 79
        is_day (int): e.g. 1
        condition (Condition): See above
        wind_mph (float): e.g. 9.4
        wind_kph (float): e.g. 15.1
        wind_degree (int): e.g. 204
        wind_dir (str): e.g. "SSW", "WSW"
        pressure_mb (int): e.g. 1013
        pressure_in (float): e.g. 29.91
        precip_mm (int): e.g. 0
        precip_in (int): e.g. 0
        humidity (int): e.g. 39
        cloud (int): e.g. 0
        feelslike_c (float): e.g. 26.1
        feelslike_f (float): e.g. 79
        windchill_c (float): e.g. 24.3
        windchill_f (float): e.g. 75.7
        heatindex_c (float): e.g. 24.9
        heatindex_f (float): e.g. 76.8
        dewpoint_c (float): e.g. 9.7
        dewpoint_f (float): e.g. 49.4
        vis_km (float): e.g. 10
        vis_miles (float): e.g. 6
        uv (float): e.g. 10.6
        gust_mph (float): e.g. 10.8
        gust_kph (float): e.g. 17.4
        short_rad (float): e.g. 1014.66
        diff_rad (float): e.g. 138.6
        dni (float): Direct Normal Irradiance (intensity of sunlight) e.g. 0
        gti (float): Global Tilted Irradiance (total sunlight for solar panels) e.g. 145.36
    """

    last_updated_epoch: int
    last_updated: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: int
    pressure_in: float
    precip_mm: int
    precip_in: int
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    vis_km: float
    vis_miles: float
    uv: float
    gust_mph: float
    gust_kph: float
    short_rad: float
    diff_rad: float
    dni: float
    gti: float


class Day(BaseModel):
    """
    Daily overview (i.e. max, min, average, total) of the location, as returned by Weather API

    Args:
        maxtemp_c (float): e.g. 24.2
        maxtemp_f (float): e.g. 75.6
        mintemp_c (float): e.g. 12.7
        mintemp_f (float): e.g. 54.8
        avgtemp_c (float): e.g. 18.5
        avgtemp_f (float): e.g. 65.4
        maxwind_mph (float): e.g. 10.7
        maxwind_kph (float): e.g. 17.3
        totalprecip_mm (float): e.g. 0
        totalprecip_in (float): e.g. 0
        totalsnow_cm (float): e.g. 0
        avgvis_km (float): e.g. 10
        avgvis_miles (float): e.g. 6
        avghumidity (int): Average humidity as percentage. e.g. 60
        daily_will_it_rain (bool): e.g. 0
        daily_chance_of_rain (int): Chance of rain as percentage. e.g. 0
        daily_will_it_snow (bool): e.g. 0
        daily_chance_of_snow (int): Chance of snow as percentage. e.g. 0
        condition (Condition): See above
        uv (float): e.g. 3.3
    """

    maxtemp_c: float
    maxtemp_f: float
    mintemp_c: float
    mintemp_f: float
    avgtemp_c: float
    avgtemp_f: float
    maxwind_mph: float
    maxwind_kph: float
    totalprecip_mm: float
    totalprecip_in: float
    totalsnow_cm: float
    avgvis_km: float
    avgvis_miles: float
    avghumidity: int
    daily_will_it_rain: bool
    daily_chance_of_rain: int
    daily_will_it_snow: bool
    daily_chance_of_snow: int
    condition: Condition
    uv: float


class Astro(BaseModel):
    """
    Astrological (i.e. sun & moon) information, as returned by Weather API

    Args:
        sunrise (str): e.g. "06:02 AM"
        sunset (str): e.g. "08:45 PM"
        moonrise (str): e.g. "08:00 PM"
        moonset (str): e.g. "04:00 AM"
        moon_phase (str): e.g. "Waxing Gibbous"
        moon_illumination (int): e.g. 97
        is_moon_up (bool): e.g. 1
        is_sun_up (bool): e.g. 0
    """

    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moon_phase: str
    moon_illumination: int
    is_moon_up: bool
    is_sun_up: bool


class Hour(BaseModel):
    """
    Information to cover a single hour of weather, as returned by Weather API.
    Note `Hours` is a list of this `Hour` class

    Args:
        time_epoch (int): e.g. 1767272400
        time (str): Start time for the hour, e.g. "2026-01-02 00:00"
        temp_c (float): e.g. 15.4
        temp_f (float): e.g. 59.7
        is_day (int): e.g. 0
        condition (Condition): See above
        wind_mph (float): e.g. 9.2
        wind_kph (float): e.g. 14.8
        wind_degree (float): e.g. 173
        wind_dir (str): e.g. "S"
        pressure_mb (float): e.g. 1016
        pressure_in (float): e.g. 29.99
        precip_mm (float): e.g. 0
        precip_in (float): e.g. 0
        snow_cm (float): e.g. 0
        humidity (float): e.g. 70
        cloud (float): e.g. 0
        feelslike_c (float): e.g. 15.4
        feelslike_f (float): e.g. 59.6
        windchill_c (float): e.g. 15.4
        windchill_f (float): e.g. 59.6
        heatindex_c (float): e.g. 15.4
        heatindex_f (float): e.g. 59.6
        dewpoint_c (float): e.g. 9.9
        dewpoint_f (float): e.g. 49.8
        will_it_rain (bool): e.g. 0
        chance_of_rain (int): Chance of rain as percentage. e.g. 0
        will_it_snow (bool): e.g. 0
        chance_of_snow (int): Chance of snow as percentage. e.g. 0
        vis_km (float): e.g. 10
        vis_miles (float): e.g. 6
        gust_mph (float): e.g. 13.5
        gust_kph (float): e.g. 21.8
        uv (float): e.g. 0
        short_rad (float): e.g. 0
        diff_rad (float): e.g. 0
        dni (float): Direct Normal Irradiance (intensity of sunlight) e.g. 0
        gti (float): Global Tilted Irradiance (total sunlight for solar panels) e.g. 145.36
    """

    time_epoch: int
    time: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: float
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    snow_cm: float
    humidity: float
    cloud: float
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    will_it_rain: bool
    chance_of_rain: int
    will_it_snow: bool
    chance_of_snow: int
    vis_km: float
    vis_miles: float
    gust_mph: float
    gust_kph: float
    uv: float
    short_rad: float
    diff_rad: float
    dni: float
    gti: float


class Hours(BaseModel):
    """
    A list of each 'Hour' object to describe a day.  
    Note that hours that have already passed are blank
    """
    List[Hour]


class Forecast_Day(BaseModel):
    """
    The total information returned by Weather API for a day.

    Args:
        date (str): e.g. "2026-01-02"
        date_epoch (int): e.g. 1767312000
        day (Day): See above
        astro (Astro): See above
        hour (List[Hour]): See above
    """

    date: str
    date_epoch: int
    day: Day
    astro: Astro
    hour: List[Hour]


class Forecast(BaseModel):
    """
    The forecast conditions for the following days

    Args:
        forecastday (List[Forecast_Day]) : A list of each days total information
    """
    forecastday: List[Forecast_Day]


class Current_Weather(BaseModel):
    """
    The object returned by `http://api.weatherapi.com/v1/current.json`
    Contains information about the matched location, and the current weather conditions

    Args:
        location (Location): name, state, country, lat/long, timezone
        current (Current): temp, wind, uv, gust, etc.
    """

    location: Location
    current: Current


class Forecast_Weather(BaseModel):
    """
    The object returned by `http://api.weatherapi.com/v1/forecast.json`
    Contains information about the matched location, and the current weather conditions

    Args:
        location (Location): name, state, country, lat/long, timezone
        current (Current): temp, wind, uv, gust, etc.
        forecast (Forecast): daily/hourly temp, wind, uv, gust, etc.
    """

    location: Location
    current: Current
    forecast: Forecast
