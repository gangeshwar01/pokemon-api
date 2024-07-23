from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models, schemas, database, crud

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    
    async with database.SessionLocal() as db:
        await crud.fetch_and_store_pokemon(db)

@app.get("/api/v1/pokemons", response_model=list[schemas.Pokemon])
async def get_pokemons(type: str = None, name: str = None, db: AsyncSession = Depends(database.get_db)):
    query = select(models.Pokemon)
    if type:
        query = query.filter(models.Pokemon.type.contains(type))
    if name:
        query = query.filter(models.Pokemon.name.contains(name))
    
    result = await db.execute(query)
    return result.scalars().all()
