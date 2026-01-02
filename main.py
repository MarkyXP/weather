from fastapi import FastAPI
from app.api import weather

app = FastAPI()

app.include_router(weather.router, prefix="/api/v1/weather", tags=["Weather"])
#app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)