from pydantic import BaseModel

class Actor(BaseModel):
    id: int
    first_name: str
    last_name: str
    ranking: int
    has_oscar: bool