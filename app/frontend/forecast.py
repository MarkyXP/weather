
import asyncio

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.utils import update_weather

router = APIRouter()

templates = Jinja2Templates(directory="app/pages")

@router.get("/forecast", response_class=HTMLResponse)
async def list_crs(request: Request):
    
    # Return only the list fragment so HTMX can swap it in
    return templates.TemplateResponse(
        "partial_crs_list.html",
        {"request": request, "docs": None}
    )