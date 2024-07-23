import requests
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=1000"

async def fetch_and_store_pokemon(db: AsyncSession):
    response = requests.get(POKEAPI_URL)
    pokemons = response.json().get("results", [])
    
    for pokemon in pokemons:
        pokemon_data = requests.get(pokemon["url"]).json()
        db_pokemon = models.Pokemon(
            id=pokemon_data["id"],
            name=pokemon_data["name"],
            image_url=pokemon_data["sprites"]["front_default"],
            type=", ".join([t["type"]["name"] for t in pokemon_data["types"]])
        )
        db.add(db_pokemon)
    
    await db.commit()
