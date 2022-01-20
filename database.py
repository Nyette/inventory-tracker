from dotenv import load_dotenv
from os import environ
from sqlmodel import SQLModel, create_engine, Session
from models import Item

load_dotenv()

database_url = environ["DATABASE_URL"]

if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(database_url, connect_args = {"connect_timeout": 10})

def create_database_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
