from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter

from src.persistence.database import initialize_database
from src.persistence.models import Author, Book

app = FastAPI()
db = initialize_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(CRUDRouter(schema=Author))
app.include_router(CRUDRouter(schema=Book))
