from fastapi import APIRouter
from pydantic import BaseModel

app = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno : str = "soy el campo interno"

@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje" : "Hola desde FastAPI", "autor": "Rahi Ruilova", "version": "0.1.0"}

@app.get("/a")
def endpoint_a() -> Mensaje:
    return Mensaje(texto="Hola")

@app.get("/b", response_model=Mensaje)
def endpoint_b():
    return {"texto": "Hola", "prioridad": 5, "campo_interno": "debería salir"}

@app.get("/ruilova")
def endpoint_ruilova() -> Mensaje:
    return Mensaje(texto = "Hola ruilova", prioridad= 5)

@app.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola rahi", "prioridad": 5, "campo_interno": "si deberia salir", "campo_extra" : "no deberia salir"}
