# 📘 Actor API – FastAPI + Poetry

Prosty mikroserwis API w Pythonie (FastAPI), który obsługuje dane o aktorach. Zawiera pełne zarządzanie zależnościami za pomocą Poetry i testy przy użyciu pytest + httpx.

---

## ✅ Wymagania
- Python 3.10+
- Poetry (do zarządzania zależnościami i środowiskiem)

---

## 🚀 Instalacja

### 1. Zainstaluj Poetry (jeśli jeszcze nie masz)

Linux/macOS:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Windows (PowerShell):
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Sprawdź:
```bash
poetry --version
```

### 2. Sklonuj repozytorium i przejdź do katalogu
```bash
git clone <repo-url>
cd actor-api
```

### 3. Zainstaluj zależności
```bash
poetry install
```

---

## 🏗️ Struktura projektu
```
actor-api/
├── pyproject.toml
├── src/
│   ├── main.py                    # Definicje endpointów
│   ├── models/
│   │   └── actor.py              # Model aktora (Pydantic)
│   └── repository/
│       └── actor_repository.py   # Operacje CRUD na danych w pamięci
└── tests/
    └── test_main.py              # Testy HTTP (pytest + httpx)
```

---

## 🔥 Uruchomienie serwera (Swagger)

```bash
poetry run uvicorn src.main:app --reload
```

### Otwórz Swagger UI:

```
http://127.0.0.1:8000/docs
```

Tam możesz:
- Przeglądać listę aktorów (`GET /actors`)
- Pobierać konkretnego aktora (`GET /actors/{id}`)
- Dodawać nowych (`POST /actors`)
- Usuwać (`DELETE /actors/{id}`)

---

## 🧪 Testowanie

```bash
poetry run pytest
```

---

## 🛠️ PyCharm – konfiguracja uruchamiania (opcjonalnie)

1. `Run > Edit Configurations`
2. ➕ Python
3. `Script path`: `uvicorn`
4. `Parameters`: `src.main:app --reload`
5. Interpreter: środowisko z Poetry

---

## 📦 Eksport zależności (opcjonalne)

```bash
poetry export -f requirements.txt --output requirements.txt
```

---

Gotowe! 🎉 Możesz teraz rozwijać projekt, dodać filtrowanie, edycję (PUT), integrację z bazą danych lub Docker.


testy:
poetry run pytest tests/test_main.py
