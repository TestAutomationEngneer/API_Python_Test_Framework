from typing import Dict, Optional
from src.models.actor import ActorCreate, ActorResponse

# In-memory "database"
_actors: Dict[int, ActorResponse] = {}

# Internal ID counter
_id_counter = 5

# Initial test data
for i, (fn, ln, rank, oscar) in enumerate([
    ("Tom", "Hanks", 1, True),
    ("Morgan", "Freeman", 2, False),
    ("Meryl", "Streep", 3, True),
    ("Leonardo", "DiCaprio", 4, True),
    ("Natalie", "Portman", 5, True),
], start=1):
    _actors[i] = ActorResponse(id=i, first_name=fn, last_name=ln, ranking=rank, has_oscar=oscar)


def generate_next_id() -> int:
    global _id_counter
    _id_counter += 1
    return _id_counter


def get(actor_id: int) -> Optional[ActorResponse]:
    return _actors.get(actor_id)


def add_with_id(actor_id: int, payload: ActorCreate) -> ActorResponse:
    actor = ActorResponse(id=actor_id, **payload.dict())
    _actors[actor_id] = actor
    return actor


def get_all():
    return list(_actors.values())


def delete(actor_id: int):
    _actors.pop(actor_id, None)
