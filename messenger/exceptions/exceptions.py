"""
Custom exceptions.
"""

from http import HTTPStatus

from .base import BaseException


class NotFoundException(BaseException):
    """
    Not found exception.
    """
    code = HTTPStatus.NOT_FOUND
    error_code = HTTPStatus.NOT_FOUND
    message = HTTPStatus.NOT_FOUND.description


class IntegrityErrorException(BaseException):
    """
    Integrity error exception.
    """
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description
