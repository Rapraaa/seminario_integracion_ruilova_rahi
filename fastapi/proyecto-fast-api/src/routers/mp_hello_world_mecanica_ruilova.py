from fastapi import APIRouter
from pydantic import BaseModel

taller_router = APIRouter()

class Vehiculo(BaseModel):
    modelo: str
    prioridad: int = 1
    nota_interna: str = "soy la nota interna del taller"

@taller_router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje" : "Bienvenido al Taller Mecanico Ruilova", "mecanico": "Rahi Ruilova", "version": "0.1.0"}

@taller_router.get("/revision")
def endpoint_revision() -> Vehiculo:
    return Vehiculo(modelo="Toyota Hilux")

@taller_router.get("/orden", response_model=Vehiculo)
def endpoint_orden():
    return {"modelo": "Chevrolet Sail", "prioridad": 5, "nota_interna": "debería salir"}

@taller_router.get("/ruilova")
def endpoint_ruilova() -> Vehiculo:
    return Vehiculo(modelo = "Kia Sportage de Rahi Ruilova", prioridad= 5)

@taller_router.get("/campo-extra", response_model=Vehiculo)
def endpoint_campo_extra():
    return {"modelo": "Ford Ranger", "prioridad": 5, "nota_interna": "si deberia salir", "costo_secreto" : "no deberia salir"}
