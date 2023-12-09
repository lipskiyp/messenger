"""
FastApi messenger app initiation.
"""

from fastapi import FastAPI

from messenger.routers.api import api_router
from messenger.database import init_db
from messenger.exceptions import (
    NotFoundException,
    IntegrityErrorException,
    base_exception_handler
)
from messenger.metadata import tags_metadata


class MessengerApp:
    """
    FastAPI app.
    """
    def create_app(self) -> FastAPI:
        app = FastAPI(openapi_tags=tags_metadata)
        self.init_routers(app)
        self.init_exception_handlers(app)
        return app

    def init_routers(self, app: FastAPI) -> None:
        app.include_router(
            api_router,
            prefix="/api",
        )

    def init_exception_handlers(self, app: FastAPI) -> None:
        app.add_exception_handler(
            NotFoundException,
            base_exception_handler
        )
        app.add_exception_handler(
            IntegrityErrorException,
            base_exception_handler
        )


app = MessengerApp().create_app()


@app.on_event("startup")
async def on_startup():
    await init_db()

