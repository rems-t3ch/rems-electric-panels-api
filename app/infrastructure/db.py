from typing import Iterator
from sqlmodel import SQLModel, create_engine, Session
from app.domain.model.entities.electronic_board import ElectronicBoard

DATABASE_URL = "sqlite+aiosqlite:///./boards.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)

def create_db_and_tables() -> None:
    """
    Create the database and tables based on the SQLModel metadata.
    """
    SQLModel.metadata.create_all(engine)

def get_session() -> Iterator[Session]:
    """
    Get a new database session.
    Yields:
        Iterator[Session]: An iterator that yields a database session.
    """
    with Session(engine) as session:
        yield session