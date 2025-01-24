"""
FastAPI의 엔트리 포인트입니다.
main.py에서 구현해야 할 것들은 아래와 같습니다.

- FastAPI 객체 생성

    >>> app = FastAPI()

- 라우터 등록

    >>> app.include_router(example_router)

- 기본 라우터 생성

    >>> @app.get("/")
    >>> async def root():
    >>>     return {"message": "This is Example!"}

- 미들웨어 및 이벤트 핸들러(필요한 경우)
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .routers import reservation_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(reservation_router)

@app.get("/")
async def root():
    return FileResponse("app/static/index.html")