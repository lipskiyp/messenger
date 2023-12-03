"""
Launch FastAPI app using uvicorn.
"""

from uvicorn import run

from messenger.settings import settings


if __name__ == "__main__":
    run(
        app="messenger.server:app",
        host= settings.APP_HOST,
        port= settings.APP_PORT,
        reload=True
    )
