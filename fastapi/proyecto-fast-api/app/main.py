from fastapi import FastAPI
from routers.hello_world import app
from routers.task_router import tasks_router

router = FastAPI(title="Curso FastAPI + uv")

router.include_router(app)
router.include_router(tasks_router)
