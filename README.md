# 소개
<!--소개 써줘 형이-->
서울시립대학교

## 프로젝트 구조
```
project/
|
├── app/
│   ├── __init__.py         # FastAPI 앱 초기화
│   ├── main.py             # FastAPI 엔트리포인트 (실행 파일)
│   ├── routes/
│   │   ├── __init__.py     # 라우트 패키지 초기화
│   │   ├── reservation.py  # 예약 관련 경로 정의
│   │   └── auth.py         # 사용자 인증 관련 경로 정의
│   ├── models/
│   │   ├── __init__.py     # 데이터 모델 패키지 초기화
│   │   └── reservation.py  # 예약 데이터 모델 정의
│   ├── services/
│   │   ├── __init__.py     # 서비스 로직 패키지 초기화
│   │   └── reservation.py  # 예약 관련 비즈니스 로직
│   ├── utils/
│   │   ├── __init__.py     # 유틸리티 함수 초기화
│   │   └── validators.py   # 데이터 검증 유틸리티 함수
│   └── dependencies.py     # 의존성 관리 (예: 데이터베이스 연결, 인증)
|
├── data/
│   └── schedules.csv       # 예약 데이터 저장 파일
|
├── tests/
│   ├── __init__.py         # 테스트 패키지 초기화
│   ├── test_routes.py      # 라우트 테스트
│   ├── test_services.py    # 서비스 로직 테스트
│   └── test_models.py      # 데이터 모델 테스트
|
├── .env                    # 환경 변수 (API 키, DB 설정 등)
├── requirements.txt        # 의존성 패키지 목록
├── README.md               # 프로젝트 설명
└── run.py                  # 앱 실행 스크립트

```