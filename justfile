# Configures your environment for local development
@setup:
  poetry install
  poetry run pre-commit install

# Launches the database
@launch-infra:
  docker compose up -d

# Runs the API
@run: launch-infra
  poetry run uvicorn src.api.main:app --reload

# Runs all tests
@test:
  poetry run pytest

# Runs the formatter and import sorter
@fmt:
  poetry run black .
  poetry run isort .
  poetry run flake8 .