from fastapi import HTTPException, status

from src.messages import FILE_SIZE, INVALID_CONTENT_TYPE, OBJECT_DOES_NOT_EXISTS


class FileIsTooLarge(HTTPException):
    def __init__(self, size: int):
        self.status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
        self.detail = FILE_SIZE.format(filesize=size)


class InvalidContentType(HTTPException):
    def __init__(self, content_types: list):
        self.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        self.detail = INVALID_CONTENT_TYPE.format(
            content_types=", ".join(content_types)
        )


class ObjectDoesNotExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = OBJECT_DOES_NOT_EXISTS
