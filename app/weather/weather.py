import httpx
from fastapi import FastAPI
from contextlib import asynccontextmanager

_URL = "http://api.weatherapi.com/v1/current.json"


async def get_httpx_client(app : FastAPI):
    """
    Provides an httpx.AsyncClient instance for dependency injection.

    The client is created when the request starts and closed
    automatically after the response is sent due to the 'yield' statement.
    """
    async with httpx.AsyncClient() as client:
        app.httpx_client = client
        yield

