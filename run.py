import uvicorn
import os
from dotenv import load_dotenv

# 🔄 Załaduj zmienne środowiskowe z pliku .env
load_dotenv()



if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        reload=os.getenv("RELOAD", "false").lower() == "true"
    )