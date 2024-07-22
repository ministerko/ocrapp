import pytest
from app.database import create_db_and_tables, engine
from sqlmodel import SQLModel

@pytest.fixture(scope="function")
def setup_db():
    # Create the database and tables
    create_db_and_tables()

    yield

    # Optionally drop tables after tests
    # SQLModel.metadata.drop_all(engine)
