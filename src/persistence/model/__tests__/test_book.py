from uuid import uuid4

from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine, select
from testcontainers.postgres import PostgresContainer

from src.persistence.model.Author import Author
from src.persistence.model.Book import Book


def test_can_insert_book():
    with PostgresContainer("postgres:14") as pg:
        # Arrange
        args = FlywayCommandArgs(
            user=pg.POSTGRES_USER,
            password=pg.POSTGRES_PASSWORD,
            locations=["migrations"],
            url=f"jdbc:postgresql://localhost:{pg.get_exposed_port(5432)}/{pg.POSTGRES_DB}",
        )

        migrate(args)
        engine = create_engine(
            f"postgresql://"
            f"{pg.POSTGRES_USER}:{pg.POSTGRES_PASSWORD}"
            f"@localhost:{pg.get_exposed_port(5432)}"
            f"/{pg.POSTGRES_DB}",
            echo=True,
        )

        with Session(engine) as session:
            author = Author(id=uuid4(), name="Brando Sando")
            session.add(author)
            session.commit()

            # Act
            book = Book(
                id=uuid4(),
                author_id=author.id,
                isbn="1234-56-789",
                title="The Final Empire",
                price=13.37,
            )
            session.add(book)
            session.commit()

            # Assert
            statement = select(Book)
            results = session.exec(statement)
            retrieved_book = results.first()
            assert retrieved_book.title == book.title
            # assert retrieved_book.author.name == author.name
