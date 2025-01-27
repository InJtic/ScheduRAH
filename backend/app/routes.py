from fastapi import APIRouter
from .db import Reservation, SessionDep, itemfinder, clearweek
from datetime import datetime, date
from typing import Optional, Sequence

router = APIRouter(prefix="/api")

@router.get("/info", tags=['api'])
async def root():
    return {"message": "Hello, World!"}

@router.post("/push", tags=['api'])
async def push(reservation: Reservation, session: SessionDep) -> Reservation:
    reservation.time = datetime.strptime(reservation.time, "%Y-%m-%d %H:%M:%S")
    session.add(reservation)
    session.commit()
    session.refresh(reservation)
    return reservation

@router.get("/pull/{time}", tags=['api'])
async def pull(time: datetime, session: SessionDep) -> Optional[Sequence[Reservation]]:
    ident = {
        "time": time
    }

    reservation = itemfinder(session, ident)
    return reservation

@router.delete("/delete", tags=['api'])
async def delete(startday: date, session: SessionDep):
    clearweek(
        session,
        startday
    )
    return {"ok": True}