from uuid import UUID

from pydantic import BaseModel


class AuthorRequest(BaseModel):
    name: str


class BookRequest(BaseModel):
    isbn: str
    title: str
    price: str
    author_id: UUID
