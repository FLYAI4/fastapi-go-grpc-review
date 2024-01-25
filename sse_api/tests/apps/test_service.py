import os
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, UploadFile, File, Header
from src.apps.service import Service
from src.libs.util import delete_file
import time

apps_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
tests_path = os.path.abspath(os.path.join(apps_path, os.path.pardir))
root_path = os.path.abspath(os.path.join(tests_path, os.path.pardir))
test_img_path = os.path.abspath(os.path.join(root_path, "test_img"))


# Mock data
IMAGE = os.path.abspath(os.path.join(test_img_path, "cat.jpg"))
USERNAME = "kim"


app = FastAPI()


@app.post("/test/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(...),
    username: str = Header(default=None)
):
    result = await Service().save_image(file, username)
    return {
        "file_path": result
    }


@pytest.mark.asyncio
async def test_service_can_save_image_with_valid():
    client = TestClient(app)

    # given : 유효한 데이터(이미지)
    with open(IMAGE, "rb") as f:
        files = {"file": ("image.jpg", f, "image/jpeg")}
        # when : 로컬에 저장
        response = client.post("/test/uploadfile/",
                               files=files,
                               headers={"username": USERNAME}
                               )

    # then : 정상 처리
    assert response.status_code == 200
    result = response.json()["file_path"]
    assert result.split("/")[-1] == USERNAME + ".jpg"

    # 생성한 파일 정리
    await delete_file(result)


@pytest.mark.asyncio
async def test_service_can_send_stream_text():
    # given : 1초 에 한번씩 텍스트 생성
    async def fake_text_streamer():
        for i in range(10):
            yield f"Fake text bytes - {i}".encode()
            time.sleep(0.5)

    # when : 텍스트 전달(10초)
    async def create_text_list():
        result = []
        async for text in fake_text_streamer():
            result.append(text.decode())
        return result

    result = await create_text_list()

    # then : 총 10개의 텍스트 저장
    assert len(result) == 10
    assert result[-1] == "Fake text bytes - 9"
