from pydantic import BaseSettings

class Config(BaseSettings):
    WEATHER_API_KEY: str
    HF_TOKEN: str
    
    class Config:
        env_file = ".env"

CONFIG = Config()