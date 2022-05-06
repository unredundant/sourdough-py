from uuid import uuid4

import pytest
from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine, select
from testcontainers.postgres import PostgresContainer

from src.persistence.__tests__.util import cleanup, insert_author_with_multiple_books
from src.persistence.models import Author


def test_fucking_hell():
    with PostgresContainer("postgres:14") as pg:
        engine = create_engine(
            f"postgresql://"
            f"{pg.POSTGRES_USER}:{pg.POSTGRES_PASSWORD}"
            f"@localhost:{pg.get_exposed_port(5432)}"
            f"/{pg.POSTGRES_DB}",
            echo=True,
        )

        args = FlywayCommandArgs(
            user=pg.POSTGRES_USER,
            password=pg.POSTGRES_PASSWORD,
            locations=["migrations"],
            url=f"jdbc:postgresql://localhost:{pg.get_exposed_port(5432)}/{pg.POSTGRES_DB}",
        )
        migrate(args)

        with Session(engine) as session:
            author = Author(id=uuid4(), name="Brando Sando")
            session.add(author)
            session.commit()


@pytest.mark.skip(reason="Fucking hell")
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
    assert author_result.books == []

    # After
    cleanup(session)


@pytest.mark.skip(reason="Fucking hell")
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
