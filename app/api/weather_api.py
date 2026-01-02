from fastapi import APIRouter, Depends, Request

from app.schemas.weather_schema import \
    Current_Weather as Current_Weather_Schema
from app.schemas.weather_schema import \
    Forecast_Weather as Forecast_Weather_Schema
from app.weather import weather

router = APIRouter()


@router.get("/current")
async def get_location_current(
    request: Request, location: str
) -> Current_Weather_Schema:
    # Access the shared client instance via app.httpx_client
    client: weather.httpx.AsyncClient = request.app.httpx_client
    return await weather.get_current(client, location)


@router.get("/forecast")
async def get_location_forecast(
    request: Request, location: str
) -> Forecast_Weather_Schema:
    # Access the shared client instance via app.httpx_client
    client: weather.httpx.AsyncClient = request.app.httpx_client
    return await weather.get_forecast(client, location)
