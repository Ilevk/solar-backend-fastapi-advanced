from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import config
from app.core.lifespan import lifespan
from app.core.errors.error import BaseAPIException, BaseAuthException
from app.core.errors.handler import api_error_handler, api_auth_error_handler
from app.routers import v1_router


def get_application() -> FastAPI:
    application = FastAPI(default_response_class=ORJSONResponse, lifespan=lifespan, **config.fastapi_kwargs)

    application.include_router(v1_router)
    application.add_exception_handler(BaseAPIException, api_error_handler)
    application.add_exception_handler(BaseAuthException, api_auth_error_handler)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application

app = get_application()
