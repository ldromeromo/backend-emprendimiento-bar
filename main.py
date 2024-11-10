import os
import uvicorn

from dotenv import load_dotenv

load_dotenv()

def run_api():
    print("Iniciando servidor...")
    uvicorn.run(
        "src.routes.routes:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True
    )


if __name__ == "__main__":
    try:
        print("Entrando en el bloque principal...")
        run_api()
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Cerrando aplicación...")
        exit()
