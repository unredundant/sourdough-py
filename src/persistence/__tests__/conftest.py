import pytest
from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlalchemy.engine import Engine
from sqlmodel import create_engine
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session", autouse=True)
def engine() -> Engine:
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

        yield engine
