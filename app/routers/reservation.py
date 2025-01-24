"""
예약을 위한 라우터와 세부 기능을 구현합니다.
"""

from fastapi import APIRouter, Query
from ..models import ReservationData
from typing import Annotated

router = APIRouter(
    prefix="/reservation",
    tags=["reservation"]
)

@router.post("/")
async def add_waiting(reservation: Annotated[ReservationData, Query()] = ...):
    # TODO: 함수 구현하기
    # 데이터베이스에 예약자를 등록합니다.
    return {"message": "미구현..."}

@router.get("/")
async def read_all():
    # TODO: 함수 구현하기
    # 예약 현황 표를 그리기 위해 사용되는 함수입니다.
    return {"message": "미구현..."}