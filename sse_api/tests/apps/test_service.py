import os
import pytest
import base64
from fastapi.testclient import TestClient
from fastapi import FastAPI, UploadFile, File, Header
from src.apps.service import Service
from src.libs.util import delete_file


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
    # when : 텍스트 전달(5초)
    async def create_text_list():
        result = []
        # given : 1초 에 한번씩 텍스트 생성
        async for text in Service().send_stream_text():
            result.append(text.decode())
        return result

    result = await create_text_list()

    # then : 총 10개의 텍스트 저장
    assert len(result) == 10
    assert result[-1] == "text: Fake text bytes - 9\n"


@pytest.mark.asyncio
async def test_service_can_send_stream_text_image():
    # when : 전달
    async def create_text_list():
        result = []
        base_64_image = ""
        # given : 텍스트 전달(3초), 이미지 전달, 텍스트 전달(2초)
        async for text in Service().send_stream_text_image():
            data = text.decode()
            if data[:5] == "image":
                base_64_image = data
            else:
                result.append(data)
        return result, base_64_image

    # then : 총 10개 텍스트 저장, 이미지 파일명 동일
    result_text, result_img = await create_text_list()

    assert len(result_text) == 10
    assert result_text[-1] == "text: Fake text bytes - 9\n"

    with open(IMAGE, "rb") as f:
        image_data = f.read()
        base64_image_data = base64.b64encode(image_data).decode()

    assert result_img[7:] == base64_image_data + "\n"
