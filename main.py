from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import weather_api
from app.core.config import CONFIG
from app.database import db
from app.weather import weather


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Attach the httpx client to the app, so weather can close out the client gracefully
    async with weather.get_httpx_client(app):
        # Attach the DB to the app
        async with db.get_db(
            app=app, connection_string=CONFIG.DATABASE_CONNECTION_STRING
        ):
            yield


app = FastAPI(
    title="Weather",
    description="Forecast & current weather for a location",
    version="0.0.1",
    lifespan=lifespan,
)
app.mount(path="/static", app=StaticFiles(directory="app/static"), name="static")

app.include_router(weather_api.router, prefix="/api/v1/weather", tags=["Weather"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
