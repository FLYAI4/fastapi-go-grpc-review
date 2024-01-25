import os
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, UploadFile, File, Header
from src.libs.util import save_image_local, delete_file

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
    result = await save_image_local(file, username)
    return {
        "file_path": result
    }


@pytest.mark.asyncio
async def test_user_service_can_insert_image_with_valid():
    client = TestClient(app)

    # given : 유효한 데이터(이미지)
    with open(IMAGE, "rb") as f:
        files = {"file": ("image.jpg", f, "image/jpeg")}
        # when : DB에 저장
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
