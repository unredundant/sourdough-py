from fastapi import FastAPI

from src.persistence.database import initialize_database

app = FastAPI()
db = initialize_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}
