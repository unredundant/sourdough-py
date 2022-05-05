from datetime import datetime
from typing import List
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    id: UUID = Field(primary_key=True, nullable=False)
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    books: List["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    id: UUID = Field(primary_key=True, nullable=False)
    isbn: str
    title: str
    price: float
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    author_id: UUID = Field(foreign_key="author.id")
    author: Author = Relationship(back_populates="books")
