from sqlmodel import SQLModel, Field
from sqlalchemy import Enum
from typing import Annotated
import enum
from datetime import datetime

class Club(str, enum.Enum):
    INDEPENDENT = "무소속"
    RAH = "라"

class Reservation(SQLModel, table=True):
    id: Annotated[int, Field(default=None, primary_key=True)]

    # 고객 정보
    name: Annotated[str, Field(max_length=10)]
    club: Annotated[Club, Field(sa_column=Enum(Club, native_enum=False), default=Club.INDEPENDENT)]

    # 예약 정보
    time: datetime
