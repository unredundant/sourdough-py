from uuid import uuid4

from sqlmodel import Session, select

from src.persistence.models import Author, Book


def insert_author_with_multiple_books(session: Session) -> Author:
    author = Author(id=uuid4(), name="Brando Sando")

    book_a = Book(
        id=uuid4(),
        author_id=author.id,
        isbn="1234-56-789",
        title="The Final Empire",
        price=13.37,
    )

    book_b = Book(
        id=uuid4(),
        author_id=author.id,
        isbn="1234-56-987",
        title="The Lost Metal",
        price=13.37,
    )

    session.add(author)
    session.add(book_a)
    session.add(book_b)
    session.commit()

    return author


def cleanup(session: Session):
    for book in session.exec(select(Book)).all():
        session.delete(book)
    for author in session.exec(select(Author)).all():
        session.delete(author)
    session.commit()
