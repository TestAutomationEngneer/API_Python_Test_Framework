import pytest
import httpx

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="module")
def http_client():
    with httpx.Client(base_url=BASE_URL) as client:
        yield client