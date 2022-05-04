from datetime import datetime
from uuid import UUID

from sqlmodel import Field, SQLModel


class Author(SQLModel, table=True):
    id: UUID = Field(primary_key=True, nullable=False)
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class Book(SQLModel, table=True):
    id: UUID = Field(primary_key=True, nullable=False)
    isbn: str
    title: str
    price: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    author_id: UUID = Field(foreign_key="author.id")
