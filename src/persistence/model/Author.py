from datetime import datetime
from uuid import UUID

from sqlmodel import Field, SQLModel


class Author(SQLModel, table=True):
    id: UUID = Field(primary_key=True)
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
