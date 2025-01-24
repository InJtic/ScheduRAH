"""
예약 데이터 등 데이터 모델을 정의합니다.
"""

from pydantic import BaseModel, Field, model_validator
from typing import Optional, Self
from datetime import datetime, timedelta
from enum import Enum

# 동아리 목록
class Club(str, Enum):
    independent     = "무소속"
    RAH             = "라"

# 동아리 담당자
CLUB_MANAGER = {
    Club.RAH: "김건우"
}

# 예약 데이터
class Reservation(BaseModel, extra="forbid"):
    club: Club = Field(default=Club.independent)                # 동아리명
    time: datetime                                              # 예약 (시작) 시간
    period: timedelta                                           # 예약 기간
    applicant: Optional[str] = Field(None, max_length=10)       # 지원자. 기본값은 동아리 담당자

    @model_validator(mode="after")
    def verifier(self) -> Self:
        if self.club == Club.independent and self.applicant is None:
            raise ValueError("무소속인 경우 지원자명이 입력되어야 합니다.")
        return self