"""
Base exception and exception handler.
"""

from fastapi import Request
from fastapi.responses import JSONResponse


class BaseException(Exception):
    """
    Base exception.
    """
    def __init__(self, message: str = None):
        if message:
            self.message = message


def base_exception_handler(request: Request, exception: BaseException):
    """
    Base exception handler.
    """
    return JSONResponse(
        status_code=exception.error_code,
        content={"msg": exception.message}
    )
