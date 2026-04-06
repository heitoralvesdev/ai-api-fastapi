from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pergunta(BaseModel):
    pergunta: str

@app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso"}

@app.post("/perguntar")
def responder(pergunta: Pergunta):
    if "etl" in pergunta.pergunta.lower():
        resposta = "ETL significa Extração, Transformação e Carga de dados."
    else:
        resposta = "Ainda estou aprendendo, mas posso melhorar!"

    return {"resposta": resposta}
