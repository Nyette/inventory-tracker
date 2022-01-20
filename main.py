from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import items
from database import create_database_and_tables

app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name = "static")

templates = Jinja2Templates(directory = "templates")

app.include_router(items.router)

@app.on_event("startup")
def on_startup():
    create_database_and_tables()

@app.get("/", response_class = HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
