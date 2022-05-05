from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter

from src.api.models import AuthorRequest, BookRequest
from src.persistence.database import get_database_session, run_migrations
from src.persistence.models import Author, Book

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    run_migrations()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(
    CRUDRouter(
        create_schema=AuthorRequest,
        update_schema=AuthorRequest,
        db=get_database_session,
        db_model=Author,
        schema=Author,
    )
)

app.include_router(
    CRUDRouter(
        create_schema=BookRequest,
        update_schema=BookRequest,
        db=get_database_session,
        db_model=Book,
        schema=Book,
    )
)
