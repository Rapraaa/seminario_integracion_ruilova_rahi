from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

vehiculos_router = APIRouter()


class VehiculoCreate(BaseModel):
    modelo: str = Field(min_length=3, max_length=100)
    falla: str | None = None
    prioridad: str = "media"
    servicios: list[str] = Field(default_factory=list)


class VehiculoRead(BaseModel):
    id: int
    modelo: str
    falla: str | None
    prioridad: str
    servicios: list[str]
    esta_reparado: bool


class VehiculoUpdate(BaseModel):
    modelo: str | None = Field(default=None, min_length=3, max_length=100)
    falla: str | None = None
    prioridad: str | None = None
    servicios: list[str] | None = None
    esta_reparado: bool | None = None


VEHICULOS: list[dict] = [
    {
        "id": 1,
        "modelo": "Toyota Hilux",
        "falla": "Ruido en los frenos",
        "prioridad": "alta",
        "servicios": ["Frenos"],
        "esta_reparado": False,
    },
    {
        "id": 2,
        "modelo": "Chevrolet Sail",
        "falla": None,
        "prioridad": "media",
        "servicios": ["Cambio de aceite", "Alineacion"],
        "esta_reparado": False,
    },
]
NEXT_ID = 3



@vehiculos_router.post("/vehiculos", response_model=VehiculoRead, status_code=201)
def create_vehiculo(vehiculo: VehiculoCreate) -> dict:
    global NEXT_ID
    nuevo_vehiculo = {
        "id": NEXT_ID,
        "esta_reparado": False,
        "notas_internas": "registrado por Rahi Ruilova",
        **vehiculo.model_dump(),
    }
    VEHICULOS.append(nuevo_vehiculo)
    NEXT_ID += 1
    return nuevo_vehiculo


@vehiculos_router.get("/vehiculos", response_model=list[VehiculoRead])
def list_vehiculos() -> list[dict]:
    return VEHICULOS


@vehiculos_router.patch("/vehiculos/{vehiculo_id}", response_model=VehiculoRead)
def update_vehiculo(vehiculo_id: int, update: VehiculoUpdate) -> dict:
    for vehiculo in VEHICULOS:
        if vehiculo["id"] == vehiculo_id:
            cambios = update.model_dump(exclude_unset=True)
            vehiculo.update(cambios)
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")


@vehiculos_router.post("/vehiculos/from-model")
def create_from_model(vehiculo: VehiculoCreate) -> dict:
    global NEXT_ID
    data = vehiculo.model_dump()
    nuevo_vehiculo = {"id": NEXT_ID, "esta_reparado": False, **data}
    VEHICULOS.append(nuevo_vehiculo)
    NEXT_ID += 1

    validado = VehiculoRead.model_validate(nuevo_vehiculo)
    return validado.model_dump()


@vehiculos_router.get("/vehiculos/{vehiculo_id}/raw-vs-validated")
def compare_raw_validated(vehiculo_id: int) -> dict:
    raw = next((v for v in VEHICULOS if v["id"] == vehiculo_id), None)
    if raw is None:
        return {"error": "no encontrado"}

    validado = VehiculoRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validado.model_dump(),
        "validated_model_dump_json": validado.model_dump_json(),
    }


@vehiculos_router.delete("/vehiculos/{vehiculo_id}", status_code=204)
def delete_vehiculo(vehiculo_id: int) -> None:
    for index, vehiculo in enumerate(VEHICULOS):
        if vehiculo["id"] == vehiculo_id:
            VEHICULOS.pop(index)
            return
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")


@vehiculos_router.get("/vehiculos/{vehiculo_id}", response_model=VehiculoRead)
def get_vehiculo(vehiculo_id: int) -> dict:
    for vehiculo in VEHICULOS:
        if vehiculo["id"] == vehiculo_id:
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
