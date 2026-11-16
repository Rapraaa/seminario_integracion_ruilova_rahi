from fastapi import FastAPI
from routers.hello_world import app

router = FastAPI(title="Curso FastAPI + uv")

router.include_router(app)
