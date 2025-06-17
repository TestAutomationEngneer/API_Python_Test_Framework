# 📁 tests/test_httpx_sync.py
# Testy synchroniczne z użyciem httpx.Client + logowanie — wymagają uruchomionego serwera FastAPI

import httpx
import random
import logging
import sys

# 🔧 Konfiguracja logowania — wymuszenie wyświetlania w pytest
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.handlers = [handler]

BASE_URL = "http://127.0.0.1:8000"

def generate_random_id():
    return random.randint(1000, 9999)

def test_get_all_actors():
    logger.info("Test: Pobieranie wszystkich aktorów")
    with httpx.Client(base_url=BASE_URL) as client:
        response = client.get("/actors")
    assert response.status_code == 200
    actors = response.json()
    logger.info(f"Pobrano {len(actors)} aktorów: {actors}")

def test_get_single_actor():
    logger.info("Test: Pobieranie pojedynczego aktora o ID 1")
    with httpx.Client(base_url=BASE_URL) as client:
        response = client.get("/actors/1")
    assert response.status_code == 200
    actor = response.json()
    logger.info(f"Pobrano aktora: {actor}")

def test_post_new_actor():
    random_id = generate_random_id()
    new_actor = {
        "id": random_id,
        "first_name": "Test",
        "last_name": "Httpx",
        "ranking": 77,
        "has_oscar": False
    }
    logger.info(f"Test: Tworzenie nowego aktora z ID: {random_id}")
    with httpx.Client(base_url=BASE_URL) as client:
        response = client.post("/actors", json=new_actor)
    assert response.status_code == 200
    created_actor = response.json()
    logger.info(f"Utworzono aktora: {created_actor}")

def test_delete_actor():
    actor_id = generate_random_id()
    actor_to_delete = {
        "id": actor_id,
        "first_name": "Delete",
        "last_name": "Httpx",
        "ranking": 88,
        "has_oscar": True
    }
    logger.info(f"Test: Tworzenie i usuwanie aktora z ID: {actor_id}")
    with httpx.Client(base_url=BASE_URL) as client:
        post_response = client.post("/actors", json=actor_to_delete)
        assert post_response.status_code == 200
        logger.info(f"Utworzono aktora do usunięcia: {post_response.json()}")

        delete_response = client.delete(f"/actors/{actor_id}")
        assert delete_response.status_code == 200
        logger.info(f"Usunięto aktora: {delete_response.json()}")
