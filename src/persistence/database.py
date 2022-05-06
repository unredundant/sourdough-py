from slitherway.commands import clean, migrate
from slitherway.models import FlywayCommandArgs
from sqlmodel import Session, create_engine

MIGRATION_ARGS = migration_args = FlywayCommandArgs(
    url="jdbc:postgresql://localhost:5432/test_db",
    user="test_user",
    password="test_password",
    locations=["migrations"],
)


def get_database_session() -> Session:
    engine = create_engine(
        "postgresql://test_user:test_password@localhost:5432/test_db", echo=True
    )

    return Session(engine)


def run_migrations():
    migrate(MIGRATION_ARGS)


def clean_database():
    clean(MIGRATION_ARGS)
