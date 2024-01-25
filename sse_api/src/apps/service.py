import time
from fastapi import UploadFile
from src.libs.util import save_image_local


class Service:
    def __init__(self) -> None:
        pass

    async def save_image(self, file: UploadFile, username: str):
        result = await save_image_local(file, username)
        return result

    async def send_stream_text(self):
        for i in range(10):
            yield f"Fake text bytes - {i}".encode()
            time.sleep(0.5)
