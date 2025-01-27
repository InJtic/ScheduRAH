from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import Depends
from typing import Annotated
from .models import Reservation
from datetime import date, timedelta

engine = create_engine("sqlite:///database.db")

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def itemfinder(session: SessionDep, info: dict):
    return session.exec(
        select(Reservation).where(
            *[getattr(Reservation, key) == value
              for key, value in info.items()]
        )
    ).all()

def clearweek(session: SessionDep, startday: date):
    reservs = session.exec(
        select(Reservation).where(
            (startday <= Reservation.time) & (Reservation.time < startday + timedelta(days=7))
        )
    ).all()

    for reservation in reservs:
        session.delete(reservation)
    
    session.commit()