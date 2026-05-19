from fastapi import FastAPI
from sqlalchemy import create_engine, text
# OperationalError
import os


app = FastAPI()

# La URL se construye usando el nombre del servicio definido en docker-compose
DATABASE_URL = os.getenv("DATABASE_URL",
                         "postgresql://user:pass@db:5432/dbname")

engine = create_engine(DATABASE_URL)


@app.get("/")
def read_root():
    return {"message": "FastAPI funcionando en Docker"}


@app.get("/status")
def status():
    return {"message": "FastAPI RuizQuiros-FranciscoJavier v.2.1"}


@app.get("/db-check")
def check_db():
    try:
        # Intentamos una operación mínima
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "Conexión a la base de datos exitosa"}

    # except OperationalError:
    #     # captura error de conexión ("db" no responde o no existe)
    #     return {
    #         "status": "Error",
    #         "details": "No se ha podido establecer conexión con base de datos."
    #     }

    except Exception:
        # Captura cualquier otro error inesperado de forma genérica
        return {
            "status": "Error",
            "details": "Error interno del servidor."
        }
#Version8
# @app.get("/db-check0")
# def check_db0():
#     try:
#         with engine.connect() as connection:
#             connection.execute(text("SELECT 1"))
#         return {"status": "Conexión a la base de datos exitosa"}
#     except Exception as e:
#         return {"status": "Error", "details": str(e)}
