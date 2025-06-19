from pydantic import BaseModel, Field


class ActorCreate(BaseModel):
    first_name: str
    last_name: str
    ranking: int
    has_oscar: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Tom",
                    "last_name": "Hanks",
                    "ranking": 1,
                    "has_oscar": True
                }
            ]
        }
    }


class ActorResponse(ActorCreate):
    id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "first_name": "Tom",
                    "last_name": "Hanks",
                    "ranking": 1,
                    "has_oscar": True
                }
            ]
        }
    }
