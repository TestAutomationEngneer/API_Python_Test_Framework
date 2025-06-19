# 📁 tests/conftest.py

import pytest
import os
import logging
from httpx import Client
from dotenv import load_dotenv

from src.main import app

# 🌍 Wczytanie zmiennych środowiskowych
load_dotenv()
PORT = os.getenv("PORT", "8000")
BASE_URL = f"http://localhost:{PORT}"

# ✅ Konfiguracja logowania — musi być przed testami
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ✅ Fixture klienta HTTP do testów
@pytest.fixture(scope="module")
def client():
    with Client(base_url=BASE_URL) as client:
        yield client
