from fastapi import FastAPI
from routers.mp_hello_world_mecanica_ruilova import taller_router
from routers.mp_vehiculo_router_mecanica_ruilova import vehiculos_router

app = FastAPI(title="Taller Mecanico Ruilova - FastAPI + uv")

app.include_router(taller_router)
app.include_router(vehiculos_router)
