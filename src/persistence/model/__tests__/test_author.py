from uuid import uuid4

from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine, select
from testcontainers.postgres import PostgresContainer

from src.persistence.model.Author import Author


def test_can_insert_author():
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
            # Act
            author = Author(id=uuid4(), name="Brando Sando")
            session.add(author)
            session.commit()

            # Assert
            statement = select(Author)
            results = session.exec(statement)
            assert results.first().name == "Brando Sando"
