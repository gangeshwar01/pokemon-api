# Pokemon API

This project serves a list of Pokémon with their name, image, and type using FastAPI and PostgreSQL.

## Setup Instructions

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the PostgreSQL database and update the connection string in `app/config.py`
5. Run the FastAPI application
    ```sh
    uvicorn app.main:app --reload
    ```

## Endpoints

### GET /api/v1/pokemons

- Query Parameters:
  - `type`: Filter by Pokémon type
  - `name`: Filter by Pokémon name

Example: `/api/v1/pokemons?type=fire&name=char`

## Notes

- The Pokémon data is fetched from the [PokeAPI](https://pokeapi.co/) and stored in a PostgreSQL database.
