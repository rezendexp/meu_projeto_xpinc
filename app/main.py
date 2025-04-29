from fastapi import FastAPI

from fastapi import FastAPI
from .database import migrar_dados

app = FastAPI()

@app.get("/")
def home():
    return {"message": "XP Inc. - Migrador de Dados"}

@app.post("/migrar")
def migrar():
    migrar_dados()
    return {"status": "Migração concluída!"}