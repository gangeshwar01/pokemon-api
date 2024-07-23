from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    image_url: str
    type: str

    class Config:
        orm_mode = True
