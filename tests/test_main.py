from tests.utils.logging import logger
from tests.utils.data_loader import load_actor_data_with_random_id


def test_get_all_actors(http_client):
    logger.info("Test: Pobieranie wszystkich aktorów")
    response = http_client.get("/actors")
    assert response.status_code == 200
    logger.info(f"Pobrano {len(response.json())} aktorów: {response.json()}")


def test_get_single_actor(http_client):
    logger.info("Test: Pobieranie pojedynczego aktora o ID 1")
    response = http_client.get("/actors/1")
    assert response.status_code == 200
    logger.info(f"Pobrano aktora: {response.json()}")


def test_post_new_actor(http_client):
    new_actor = load_actor_data_with_random_id()
    logger.info(f"Test: Tworzenie nowego aktora z ID: {new_actor['id']}")
    response = http_client.post("/actors", json=new_actor)
    assert response.status_code == 200
    logger.info(f"Utworzono aktora: {response.json()}")


def test_delete_actor(http_client):
    actor_to_delete = load_actor_data_with_random_id()
    logger.info(f"Test: Tworzenie i usuwanie aktora z ID: {actor_to_delete['id']}")
    post = http_client.post("/actors", json=actor_to_delete)
    assert post.status_code == 200
    logger.info(f"Utworzono do usunięcia: {post.json()}")

    delete = http_client.delete(f"/actors/{actor_to_delete['id']}")
    assert delete.status_code == 200
    logger.info(f"Usunięto: {delete.json()}")
