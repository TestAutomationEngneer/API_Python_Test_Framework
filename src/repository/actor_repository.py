from typing import Dict
from src.models.actor import Actor

actors_db: Dict[int, Actor] = {
    1: Actor(id=1, first_name="Leonardo", last_name="DiCaprio", ranking=5, has_oscar=True),
    2: Actor(id=2, first_name="Tom", last_name="Hanks", ranking=2, has_oscar=True),
    3: Actor(id=3, first_name="Meryl", last_name="Streep", ranking=3, has_oscar=True),
    4: Actor(id=4, first_name="Brad", last_name="Pitt", ranking=7, has_oscar=True),
    5: Actor(id=5, first_name="Scarlett", last_name="Johansson", ranking=8, has_oscar=False),
}
def get_all() -> list[Actor]:
    return list(actors_db.values())

def get(actor_id: int) -> Actor | None:
    return actors_db.get(actor_id)

def add(actor: Actor):
    actors_db[actor.id] = actor

def delete(actor_id: int):
    del actors_db[actor_id]