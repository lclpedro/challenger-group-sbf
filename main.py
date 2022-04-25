import logging

from fastapi import FastAPI
from fastapi.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from config import settings
from src.routers.v1 import router as v1_router

logger = logging.Logger(__name__)


def get_app() -> FastAPI:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=[
                str(origin) for origin in settings.rest_application_url_cors
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]

    app = FastAPI(
        middleware=middleware,
        title=settings.rest_application_name,
        description=settings.rest_application_description,
        openapi_url="/api/openapi.json",
    )

    app.include_router(v1_router)

    return app


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting application ..")
    log_dict_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(process)d] [%(name)s] [%(levelname)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "default": {
                "level": settings.rest_application_log_level.upper(),
                "formatter": "standard",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "": {
                "handlers": ["default"],
                "level": settings.rest_application_log_level.upper(),
                "propagate": False,
            },
        },
    }
    uvicorn.run(
        "main:get_app",
        workers=settings.rest_application_workers,
        host=settings.rest_application_host,
        port=settings.rest_application_port,
        reload=settings.rest_application_reload,
        log_level=settings.rest_application_log_level.lower(),
        log_config=log_dict_config,
        factory=True,
    )
