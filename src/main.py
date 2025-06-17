from fastapi import FastAPI, HTTPException
from typing import List
from src.models.actor import Actor
from src.repository import actor_repository as repo

app = FastAPI()

@app.get("/actors", response_model=List[Actor])
def get_all_actors():
    return repo.get_all()

@app.get("/actors/{actor_id}", response_model=Actor)
def get_actor(actor_id: int):
    actor = repo.get(actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@app.post("/actors", response_model=Actor)
def create_actor(actor: Actor):
    if repo.get(actor.id):
        raise HTTPException(status_code=400, detail="Actor ID already exists")
    repo.add(actor)
    return actor

@app.delete("/actors/{actor_id}")
def delete_actor(actor_id: int):
    if not repo.get(actor_id):
        raise HTTPException(status_code=404, detail="Actor not found")
    repo.delete(actor_id)
    return {"detail": "Actor deleted"}
