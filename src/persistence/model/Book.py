from datetime import datetime
from uuid import UUID

from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: UUID = Field(primary_key=True)
    author_id: UUID = Field(foreign_key="author.id")
    isbn: str
    title: str
    price: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
