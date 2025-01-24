"""
routers 폴더를 파이썬이 패키지로 인식할 수 있도록 하기 위한 파일입니다.

하위 파일들에서 정의된 라우터들을 불러오고, 필요한 경우 재정의합니다.

예시)
>>> from example import router as example_router
"""

from .reservation import router as reservation_router