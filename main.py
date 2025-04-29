from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "Olá XP Inc.! API rodando com PyCharm!"}


@app.get("/clientes/{id}")
def buscar_cliente(id: int):
    return {"id": id, "nome": "Carlos Silva", "investimentos": 5000}
