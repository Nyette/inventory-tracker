from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from database import get_session
from models import Item

templates = Jinja2Templates(directory = "templates")

router = APIRouter(prefix = "/items", tags = ["items"])

@router.get("/", response_class = HTMLResponse)
def get_items(request: Request, session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})

@router.get("/create", response_class = HTMLResponse)
def get_create_item_form(request: Request):
    return templates.TemplateResponse("item_create.html", {"request": request})

@router.post("/create")
def create_item(name: str = Form(...), description: str = Form(...), count: int = Form(...), session: Session = Depends(get_session)):
    item = Item(name = name, description = description, count = count)
    session.add(item)
    session.commit()
    session.refresh(item)
    return RedirectResponse("/items", status_code = 303)

@router.get("/{id}", response_class = HTMLResponse)
def get_item(request: Request, id: int, session: Session = Depends(get_session)):
    item = session.get(Item, id)
    return templates.TemplateResponse("item.html", {"request": request, "item": item})

@router.get("/{id}/delete")
def delete_item(id: int, session: Session = Depends(get_session)):
    item = session.get(Item, id)
    session.delete(item)
    session.commit()
    return RedirectResponse("/items", status_code = 303)

@router.get("/{id}/update", response_class = HTMLResponse)
def get_update_item_form(request: Request, id: int, session: Session = Depends(get_session)):
    item = session.get(Item, id)
    return templates.TemplateResponse("item_update.html", {"request": request, "item": item})

@router.post("/{id}/update")
def update_item(id: int, name: str = Form(...), description: str = Form(...), count: int = Form(...), session: Session = Depends(get_session)):
    item = session.get(Item, id)
    item.name = name
    item.description = description
    item.count = count
    session.add(item)
    session.commit()
    session.refresh(item)
    return RedirectResponse("/items", status_code = 303)
