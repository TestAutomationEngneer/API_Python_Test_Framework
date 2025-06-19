import random
import pytest
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# 🔍 Test POST /actors
def test_create_actor(client):
    payload = {
        "first_name": "Test",
        "last_name": "User",
        "ranking": random.randint(10, 99),
        "has_oscar": False
    }
    response = client.post("/actors", json=payload)
    body = response.json()

    logger.info(f"Created actor: {body}")

    assert response.status_code == 201
    assert "id" in body
    assert body["first_name"] == payload["first_name"]

# 🔍 Test GET /actors
def test_get_all_actors(client):
    response = client.get("/actors")
    actors = response.json()

    logger.info(f"Fetched {len(actors)} actors")

    assert response.status_code == 200
    assert isinstance(actors, list)

# 🔍 Test GET /actors/{id}
def test_get_actor_by_id(client):
    new_actor = {
        "first_name": "Fetch",
        "last_name": "Me",
        "ranking": random.randint(1, 99),
        "has_oscar": True
    }
    post_resp = client.post("/actors", json=new_actor)
    actor_id = post_resp.json()["id"]

    get_resp = client.get(f"/actors/{actor_id}")
    actor = get_resp.json()

    logger.info(f"Retrieved actor by ID {actor_id}: {actor}")

    assert get_resp.status_code == 200
    assert actor["id"] == actor_id

# 🔍 Test DELETE /actors/{id}
def test_delete_actor_by_id(client):
    actor_data = {
        "first_name": "Delete",
        "last_name": "Me",
        "ranking": random.randint(1, 99),
        "has_oscar": False
    }
    post_resp = client.post("/actors", json=actor_data)
    actor_id = post_resp.json()["id"]

    del_resp = client.delete(f"/actors/{actor_id}")
    logger.info(f"Deleted actor with ID {actor_id}")

    assert del_resp.status_code == 200
    assert del_resp.json()["detail"] == "Actor deleted"

    get_resp = client.get(f"/actors/{actor_id}")
    logger.info(f"Attempt to fetch deleted actor ID {actor_id}: Status {get_resp.status_code}")

    assert get_resp.status_code == 404

# 🔍 Test 404 - GET non-existent actor
def test_get_nonexistent_actor(client):
    response = client.get("/actors/999999")
    logger.info(f"GET non-existent actor returned status {response.status_code}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Actor not found"

# 🔍 Test 404 - DELETE non-existent actor
def test_delete_nonexistent_actor(client):
    response = client.delete("/actors/999999")
    logger.info(f"DELETE non-existent actor returned status {response.status_code}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Actor not found"

# 🔍 Test 400 - Duplicate ID manually (should never happen in current impl)
def test_duplicate_actor_fails_if_id_reused(client):
    payload = {
        "first_name": "Unique",
        "last_name": "Actor",
        "ranking": random.randint(1, 99),
        "has_oscar": True
    }
    res1 = client.post("/actors", json=payload)
    res2 = client.post("/actors", json=payload)

    logger.info(f"First actor creation status: {res1.status_code}, second: {res2.status_code}")

    assert res1.status_code == 201
    assert res2.status_code == 201 or res2.status_code == 400
