from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Taller Mecanico Ruilova - FastAPI + uv")

class Vehiculo(BaseModel):
    modelo: str
    prioridad: int = 1
    nota_interna: str = "soy la nota interna del taller"

@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje" : "Bienvenido al Taller Mecanico Ruilova", "mecanico": "Rahi Ruilova", "version": "0.1.0"}

@app.get("/revision")
def endpoint_revision() -> Vehiculo:
    return Vehiculo(modelo="Toyota Hilux")

@app.get("/orden", response_model=Vehiculo)
def endpoint_orden():
    return {"modelo": "Chevrolet Sail", "prioridad": 5, "nota_interna": "debería salir"}

@app.get("/ruilova")
def endpoint_ruilova() -> Vehiculo:
    return Vehiculo(modelo = "Kia Sportage de Rahi Ruilova", prioridad= 5)

@app.get("/campo-extra", response_model=Vehiculo)
def endpoint_campo_extra():
    return {"modelo": "Ford Ranger", "prioridad": 5, "nota_interna": "si deberia salir", "costo_secreto" : "no deberia salir"}
