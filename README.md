# Rems Electric Panels API

## Summary
Rems Electric Panels API is a RESTful service for managing electronic panels (electronic boards). It illustrates development with Python, FastAPI Framework, and SQLModel with SQLAlchemy on SQLite Database. It also illustrates OpenAPI documentation configuration and integration with Swagger UI.

## Features
- RESTful API
- OpenAPI Documentation
- Swagger UI
- FastAPI Framework
- SQLModel with SQLAlchemy
- Async Database Operations
- Pydantic Validation
- SQLite Database (with aiosqlite driver)
- Layered Architecture

## Layers
This version of Rems Electric Panels API follows a layered architecture pattern organized into four main layers: Models, Repositories, Infrastructure, and Interfaces.

### Models Layer

The Models Layer is responsible for defining the data structures and business rules of the application. It includes the following components:

#### Entities
- **ElectronicBoard**: Represents an electronic panel with attributes such as name, model, year manufactured, year installed, and state.

#### Value Objects
- **BoardState**: An enumeration representing the operational state of a board (`operative`, `maintenance`, `out_of_service`).

#### Validation Rules
The models enforce the following business rules through Pydantic validators:
- `year_installed` must be greater than or equal to `year_manufactured`.
- `state` must be one of the predefined valid states.

### Repositories Layer

The Repositories Layer provides an abstraction for data access operations. It includes the following features:

#### Repository Interface
- Abstract definition of CRUD operations for Electronic Boards.
- Async method signatures for non-blocking database operations.

#### Repository Implementation
- **ElectronicBoardSQLModelRepository**: Concrete implementation using SQLModel and async SQLAlchemy.
- Uses per-call sessions with proper transaction management.
- Implements create, read, update, and delete operations.

### Infrastructure Layer

The Infrastructure Layer is responsible for managing database connections and configuration. Its features include:

- Database engine setup using async SQLAlchemy with SQLite.
- Async session factory configuration.
- Database initialization helper (`init_db()`) to create tables.
- Session management utilities for dependency injection.

### Interfaces Layer (REST API)

The Interfaces Layer exposes the application functionality through HTTP endpoints. It includes the following components:

#### Resources (DTOs)
Data Transfer Objects for API requests and responses:
- **ElectronicBoardCreateResource**: Payload for creating a new board.
- **ElectronicBoardUpdateResource**: Payload for updating an existing board.
- **ElectronicBoardResource**: Response model for board data.
- **ElectronicBoardListResource**: Response model for list operations.
- **ElectronicBoardDeleteResource**: Response model for delete operations.

Resources are intentionally kept as simple DTOs without business validation logic.

#### Assemblers (Transformers)
- **ElectronicBoardAssembler**: Handles conversion between model entities and resource DTOs.
- Provides bidirectional mapping methods:
  - `to_resource()`: Convert entity to response DTO.
  - `to_entity()`: Convert create DTO to entity.
  - `update_entity()`: Update entity from update DTO.
  - `to_delete_response()`: Generate delete response message.

#### Routers (Endpoints)
RESTful endpoints for Electronic Board management:
- **POST** `/boards` — Create a new Electronic Board.
- **GET** `/boards` — Get all Electronic Boards.
- **GET** `/boards/{id}` — Get an Electronic Board by ID.
- **PUT** `/boards/{id}` — Update an Electronic Board.
- **DELETE** `/boards/{id}` — Delete an Electronic Board.

All endpoints include proper HTTP status codes, error handling, and OpenAPI documentation.

## API Reference

### Create Electronic Board
- **Endpoint**: `POST /boards`
- **Request Body**: 
  ```json
  {
    "name": "Panel A",
    "model": "X1000",
    "year_manufactured": 2020,
    "year_installed": 2021,
    "state": "operative"
  }
  ```
- **Response**: `201 Created` with created board details.

### List All Electronic Boards
- **Endpoint**: `GET /boards`
- **Response**: `200 OK` with array of boards.

### Get Electronic Board by ID
- **Endpoint**: `GET /boards/{id}`
- **Path Parameter**: `id` (UUID)
- **Response**: `200 OK` with board details or `404 Not Found`.

### Update Electronic Board
- **Endpoint**: `PUT /boards/{id}`
- **Path Parameter**: `id` (UUID)
- **Request Body**: Same structure as create, all fields optional.
- **Response**: `200 OK` with updated board or `404 Not Found`.

### Delete Electronic Board
- **Endpoint**: `DELETE /boards/{id}`
- **Path Parameter**: `id` (UUID)
- **Response**: `200 OK` with success message or `404 Not Found`.

## Development Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rems-t3ch/rems-electric-panels-api.git
cd rems-electric-panels-api
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python -c "import asyncio; from app.infrastructure.db import init_db; asyncio.run(init_db())"
```

5. Run the application:
```bash
uvicorn app.main:app --reload --port 8000
```

6. Access the API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example Usage

### Using curl

```bash
# Create a new board
curl -X POST "http://127.0.0.1:8000/boards" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Panel A",
    "model": "X1000",
    "year_manufactured": 2020,
    "year_installed": 2021,
    "state": "operative"
  }'

# Get all boards
curl "http://127.0.0.1:8000/boards"

# Get a specific board
curl "http://127.0.0.1:8000/boards/{board-id}"

# Update a board
curl -X PUT "http://127.0.0.1:8000/boards/{board-id}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Panel A Updated",
    "state": "maintenance"
  }'

# Delete a board
curl -X DELETE "http://127.0.0.1:8000/boards/{board-id}"
```

## Project Structure

```
rems-electric-panels-api/
├── app/
│   ├── __init__.py
│   ├── main.py                          # FastAPI application entry point
│   ├── lifespan.py                      # Application lifecycle management
│   ├── domain/
│   │   ├── model/
│   │   │   ├── entities/
│   │   │   │   └── electronic_board.py  # ElectronicBoard entity
│   │   │   └── value_objects/
│   │   │       └── board_state.py       # BoardState enum
│   │   └── repositories/
│   │       └── electronic_board_repository.py  # Repository interface
│   ├── infrastructure/
│   │   ├── db.py                        # Database configuration
│   │   └── repositories/
│   │       └── electronic_board_sqlmodel_repository.py  # Repository implementation
│   └── interfaces/
│       └── rest/
│           ├── resources/
│           │   └── electronic_board_resource.py  # DTOs
│           ├── transforms/
│           │   └── electronic_board_assembler.py  # DTO/Entity mapping
│           └── routers/
│               └── electronic_board_router.py  # API endpoints
├── requirements.txt
└── README.md
```

## Reference Documentation

For further reference, please consider the following sections:

* [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
* [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
* [Pydantic V2 Documentation](https://docs.pydantic.dev/latest/)
* [SQLAlchemy Async Documentation](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
* [Uvicorn Documentation](https://www.uvicorn.org/)
* [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

## Guides

The following guides illustrate how to use some features concretely:

* [Building APIs with FastAPI](https://fastapi.tiangolo.com/tutorial/)
* [SQLModel Tutorial](https://sqlmodel.tiangolo.com/tutorial/)
* [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
* [Async SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
* [Testing FastAPI Applications](https://fastapi.tiangolo.com/tutorial/testing/)
* [FastAPI Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/)

## License

This project is available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
