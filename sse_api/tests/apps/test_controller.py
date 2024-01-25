import os
import pytest
from fastapi.testclient import TestClient
from src.apps import create_app


apps_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
tests_path = os.path.abspath(os.path.join(apps_path, os.path.pardir))
root_path = os.path.abspath(os.path.join(tests_path, os.path.pardir))
test_img_path = os.path.abspath(os.path.join(root_path, "test_img"))


# Mock data
IMAGE = os.path.abspath(os.path.join(test_img_path, "cat.jpg"))
USERNAME = "kim"

app = create_app()


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

# TODO : testcode 추가
# @pytest.mark.asyncio
# async def test_user_can_get_test_stream():
#     result = []
#     async with TestClient(app) as client:
#         response = await client.get("/stream/text", stream=True)
#         async for chunck in response.iter_content(10):
#             result.append(chunck.decode())
    
#     assert len(result) == 10
