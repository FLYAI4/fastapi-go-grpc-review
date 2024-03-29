from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controller import user, stream
from src.libs.error_handler import error_handlers


def create_app():
    app = FastAPI()

    # Router
    app.include_router(user)
    app.include_router(stream)

    # Handler
    error_handlers(app)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
