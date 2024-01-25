import os
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, UploadFile, File, Header, Request
from src.apps.service import Service
from src.libs.util import delete_file
from src.libs.exception import CustomHttpException
from fastapi.responses import JSONResponse


def error_handlers(app) -> JSONResponse:
    @app.exception_handler(CustomHttpException)
    async def http_custom_exception_handler(
        request: Request,
        exc: CustomHttpException
    ):
        content = {
            "meta": {
                "code": exc.code,
                "error": str(exc.error),
                "message": exc.message
            },
            "data": None
        }
        return JSONResponse(
            status_code=exc.code,
            content=content
        )


apps_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
tests_path = os.path.abspath(os.path.join(apps_path, os.path.pardir))
root_path = os.path.abspath(os.path.join(tests_path, os.path.pardir))
test_img_path = os.path.abspath(os.path.join(root_path, "test_img"))


# Mock data
IMAGE = os.path.abspath(os.path.join(test_img_path, "cat.jpg"))
USERNAME = "kim"
app = FastAPI()
error_handlers(app)


@app.post("/user/image")
async def save_image(
    file: UploadFile = File(...),
    username: str = Header(default=None)
):
    if not username:
        raise CustomHttpException(401, "No username. Please check headers.",
                                  "header error.")
    if not file:
        raise CustomHttpException(401, "No file. Please check file.",
                                  "header error.")

    result = await Service().save_image(file, username)
    await delete_file(result)
    return {
        "message": "ok",
        "username": username
    }


@pytest.fixture
def client():
    client = TestClient(app)
    yield client


@pytest.mark.asyncio
async def test_user_can_post_save_image_with_valid(client):
    # given : 유효한 username, 유효한 file
    headers = {"username": USERNAME}

    with open(IMAGE, "rb") as f:
        files = {"file": ("image.jpg", f, "image/jpeg")}

        # when : 저장 요청
        response = client.post(
            "/user/image",
            headers=headers,
            files=files)

    # then : username 반환
    assert response.status_code == 200
    assert response.json()["message"] == "ok"
    assert response.json()["username"] == USERNAME
