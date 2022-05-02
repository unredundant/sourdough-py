from uuid import uuid4

from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine

from src.persistence.model.Author import Author
from src.persistence.model.Book import Book

if __name__ == "__main__":
    migration_args = FlywayCommandArgs(
        url="jdbc:postgresql://localhost:5432/test_db",
        user="test_user",
        password="test_password",
        locations=["migrations"],
    )
    migrate(migration_args)
    engine = create_engine(
        "postgresql://test_user:test_password@localhost:5432/test_db", echo=True
    )
    session = Session(engine)
    author = Author(id=uuid4(), name="Ryan Brink")
    session.add(author)
    session.commit()

    book = Book(
        id=uuid4(),
        author_id=author.id,
        isbn="1234-56-789",
        title="The Final Empire",
        price=13.37,
    )

    session.add(book)
    session.commit()
