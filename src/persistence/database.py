from slitherway.commands import clean, migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine


def get_database_session():
    engine = create_engine(
        "postgresql://test_user:test_password@localhost:5432/test_db", echo=True
    )

    with Session(engine) as session:
        yield session


def run_migrations():
    migration_args = FlywayCommandArgs(
        url="jdbc:postgresql://localhost:5432/test_db",
        user="test_user",
        password="test_password",
        locations=["migrations"],
    )
    clean(migration_args)
    migrate(migration_args)
