from copy import deepcopy
from tests.utils.generators import generate_random_id
from tests.utils.test_data import TEST_ACTOR_TEMPLATE


def load_actor_data_with_random_id() -> dict:
    data = deepcopy(TEST_ACTOR_TEMPLATE)
    data["id"] = generate_random_id()
    return data
