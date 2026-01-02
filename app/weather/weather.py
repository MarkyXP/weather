"""
# WeatherAPI Interface

This library (`app/weather/weather.py`) interfaces with [WeatherAPI](https://www.weatherapi.com/docs/#weather-icons)
and collects either the current or the forecast weather conditions, including:
    - Queried location's match details (i.e. the matches name, region, country, lat/long, timezone)
    - Condition text
    - Temperature
    - Wind
    - Precipitation
    - UV
"""
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from app.core.config import CONFIG
from app.schemas import weather_schema


@asynccontextmanager
async def get_httpx_client(app: FastAPI):
    """
    Provides an httpx.AsyncClient instance to the FastAPI Application for
    the apps lifespan.  
    Note that it uses the yield statement, so it closes the client when the
    FastAPI app closes.

    Args:
        app (FastAPI): Adds the httpx client 
    """
    async with httpx.AsyncClient() as client:
        app.httpx_client = client
        yield


async def get_current(
    client: httpx.AsyncClient, location: str
) -> weather_schema.Current_Weather:
    """
    Get the current weather information for a location

    Args:
        client (httpx.AsyncClient): A web client to perform the get request
        location (str): Query param, could be city name, lat/long, IP, etc

    Usage:
        >>> asyncio.run(get_current(httpx.AsyncClient(), 'Melbourne'))
        Current_Weather(...)
    """
    response = await client.get(
        url=CONFIG.WEATHER_CURRENT_URL,
        params={"q": location, "key": CONFIG.WEATHER_API_KEY},
    )
    ret_val = weather_schema.Current_Weather.model_validate_json(response.content)
    return ret_val


async def get_forecast(
    client: httpx.AsyncClient, location: str
) -> weather_schema.Forecast_Weather:
    """
    Get the _forecast_ weather information for a location

    Args:
        client (httpx.AsyncClient): A web client to perform the get request
        location (str): Query param, could be city name, lat/long, IP, etc

    Usage:
        >>> asyncio.run(get_forecast(httpx.AsyncClient(), 'Melbourne'))
        Forecast_Weather(...)
    """
    response = await client.get(
        url=CONFIG.WEATHER_FORECAST_URL,
        params={"q": location, "key": CONFIG.WEATHER_API_KEY, "days": 3},
    )
    ret_val = weather_schema.Forecast_Weather.model_validate_json(response.content)
    return ret_val


if __name__ == "__main__":
    import asyncio
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
