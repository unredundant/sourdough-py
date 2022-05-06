import pytest
from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine
from testcontainers.postgres import PostgresContainer

from src.utils import get_project_root


@pytest.fixture(scope="session", autouse=True)
def session() -> Session:
    with PostgresContainer("postgres:14") as pg:
        migration_dir = "filesystem:" + str(get_project_root().resolve() / "migrations")
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
            locations=[migration_dir],
            url=f"jdbc:postgresql://localhost:{pg.get_exposed_port(5432)}/{pg.POSTGRES_DB}",
        )
        migrate(args)

        with Session(engine) as session:
            yield session
