from uuid import uuid4

from sqlmodel import select

from src.persistence.__tests__.util import cleanup, insert_author_with_multiple_books
from src.persistence.models import Author


def test_can_insert_author(session):
    # Act
    author = Author(id=uuid4(), name="Brando Sando")
    session.add(author)
    session.commit()

    # Assert
    statement = select(Author)
    results = session.exec(statement)
    author_result = results.first()
    assert author_result.name == author.name
    # assert author_result.books == []

    # After
    session.delete(author)
    session.commit()


def test_can_query_author_books(session):
    # Arrange
    author = insert_author_with_multiple_books(session)

    # Act
    statement = select(Author).where(Author.name == author.name)
    result = session.exec(statement).first()

    # Assert
    assert len(result.books) == 2

    # After
    cleanup(session)
