from random import choice, randrange

import typer
from faker import Faker

from src.persistence.database import (
    clean_database,
    get_database_session,
    run_migrations,
)
from src.persistence.models import Author, Book

app = typer.Typer()
fake = Faker()


@app.command()
def seed():
    """
    Seeds the database with some authors and books
    """
    author_count = 1000
    book_count = 10000
    run_migrations()
    authors = [Author(name=fake.name()) for _ in range(author_count)]
    books = [
        Book(
            isbn=fake.isbn10(),
            title=fake.company(),
            price=randrange(0, 25),
            author_id=choice(authors).id,
        )
        for _ in range(book_count)
    ]
    with get_database_session() as session:
        session.add_all(authors)
        session.add_all(books)
        session.commit()


@app.command()
def clean():
    """
    Completely wipes the database
    """
    clean_database()


if __name__ == "__main__":
    app()
