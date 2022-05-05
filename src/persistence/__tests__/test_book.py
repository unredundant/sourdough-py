from uuid import uuid4

from sqlmodel import select

from src.persistence.__tests__.util import cleanup, insert_author_with_multiple_books
from src.persistence.models import Author, Book


def test_can_insert_book(session):
    # Arrange
    author = Author(id=uuid4(), name="Brando Sando")
    book = Book(
        id=uuid4(),
        author=author,
        isbn="1234-56-789",
        title="The Final Empire",
        price=13.37,
    )

    # Act
    session.add(author)
    session.add(book)
    session.commit()

    # Assert
    statement = select(Book)
    results = session.exec(statement)
    retrieved_book = results.first()
    assert retrieved_book.title == book.title
    assert retrieved_book.author.name == author.name

    # After
    cleanup(session)


def test_can_query_books_by_author(session):
    # Arrange
    author = insert_author_with_multiple_books(session)

    # Act
    statement = select(Book).join(Author).where(Author.name == author.name)
    result = session.exec(statement).all()

    # Assert
    assert len(result) == 2

    # After
    cleanup(session)
