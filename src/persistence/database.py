from slitherway.commands import migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine


def initialize_database() -> Session:
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

    with Session(engine) as session:
        yield session
