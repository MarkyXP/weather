from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import weather_api
from app.weather import weather


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Attach the httpx client to the app, so weather can close out the client gracefully
    async with weather.get_httpx_client(app):
        # Attach the DB to the app
        # TODO: Add the DB
        yield


app = FastAPI(lifespan=lifespan)

app.include_router(weather_api.router, prefix="/api/v1/weather", tags=["Weather"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
