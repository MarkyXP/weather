from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    WEATHER_API_KEY: str
    WEATHER_CURRENT_URL : str = "http://api.weatherapi.com/v1/current.json"
    WEATHER_FORECAST_URL : str = "http://api.weatherapi.com/v1/forecast.json"
    HF_TOKEN: str
    DATABASE_CONNECTION_STRING : str = "sqlite:///database.db"

    model_config = SettingsConfigDict(env_file=".env")


CONFIG = Config()
