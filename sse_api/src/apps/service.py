import os
import asyncio
import base64
from fastapi import UploadFile
from src.libs.util import save_image_local

apps_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
src_path = os.path.abspath(os.path.join(apps_path, os.path.pardir))
root_path = os.path.abspath(os.path.join(src_path, os.path.pardir))
test_img_path = os.path.abspath(os.path.join(root_path, "test_img"))


class Service:
    def __init__(self) -> None:
        pass

    async def save_image(self, file: UploadFile, username: str):
        result = await save_image_local(file, username)
        return result

    async def send_stream_text(self):
        for i in range(10):
            yield f"text: Fake text bytes - {i}\n".encode()
            await asyncio.sleep(0.5)

    async def send_stream_text_image(self):
        IMAGE = os.path.abspath(os.path.join(test_img_path, "cat.jpg"))

        for i in range(6):
            yield f"text: Fake text bytes - {i}\n".encode()
            await asyncio.sleep(0.5)

        with open(IMAGE, "rb") as f:
            image_data = f.read()
            base64_image_data = base64.b64encode(image_data).decode()
        yield f"image: {base64_image_data}\n".encode()

        for i in range(6, 10):
            yield f"text: Fake text bytes - {i}\n".encode()
            await asyncio.sleep(0.5)
