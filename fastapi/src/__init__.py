from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.controller import search


def create_app():
    app = FastAPI()

    # Path
    app.include_router(search)

    # CORS
    # 참고 : CORS 정의 https://docs.tosspayments.com/resources/glossary/cors
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
