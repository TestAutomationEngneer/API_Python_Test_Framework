from fastapi import FastAPI, HTTPException, Body, Path
from typing import List

from src.models.actor import ActorCreate, ActorResponse
from src.repository import actor_repository as repo

app = FastAPI()

@app.post(
    "/actors",
    response_model=ActorResponse,
    response_description="The created actor",
    status_code=201
)
def create_actor(payload: ActorCreate = Body(..., description="Actor data to create")):
    """
    Create a new actor. The payload must include:
    - first name and last name
    - rank in top 100
    - Oscar status

    The ID will be generated automatically.
    """
    actor_id = repo.generate_next_id()
    actor = repo.add_with_id(actor_id, payload)
    return actor

@app.get(
    "/actors",
    response_model=List[ActorResponse],
    response_description="List of all actors",
    status_code=200
)
def get_all_actors():
    """
    Retrieve the list of all available actors.
    """
    return repo.get_all()

@app.get(
    "/actors/{actor_id}",
    response_model=ActorResponse,
    response_description="A single actor by ID",
    status_code=200
)
def get_actor(actor_id: int = Path(..., description="ID of the actor to retrieve")):
    """
    Get details of a single actor by their unique ID.
    """
    actor = repo.get(actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@app.delete(
    "/actors/{actor_id}",
    response_description="Delete actor by ID",
    status_code=200
)
def delete_actor(actor_id: int = Path(..., description="ID of the actor to delete")):
    """
    Delete an actor by their unique ID.
    """
    if not repo.get(actor_id):
        raise HTTPException(status_code=404, detail="Actor not found")
    repo.delete(actor_id)
    return {"detail": "Actor deleted"}
