from os import getenv
from dotenv import load_dotenv

from .config import settings


load_dotenv(getenv("messenger/.env"))


__all__ = [
    "settings",
]
