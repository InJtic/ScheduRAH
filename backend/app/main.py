from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import router
from contextlib import asynccontextmanager
from .db import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(
    title="테스트중!",
    lifespan=lifespan
)

app.include_router(router)
app.mount("/", StaticFiles(directory="test_static", html=True), name="static")

