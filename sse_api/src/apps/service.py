from fastapi import UploadFile
from src.libs.util import save_image_local


class Service:
    def __init__(self) -> None:
        pass

    async def save_image(self, file: UploadFile, username: str):
        result = await save_image_local(file, username)
        return result
