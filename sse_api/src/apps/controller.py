from fastapi import APIRouter, UploadFile, File, Header
from src.libs.exception import CustomHttpException
from src.apps.service import Service
from src.libs.util import delete_file
from fastapi.responses import StreamingResponse


user = APIRouter(prefix="/user")
stream = APIRouter(prefix="/stream")


@user.post("/image")
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


@stream.get("/text")
async def send_stream_text_image():
    return StreamingResponse(Service().send_stream_text(),
                             media_type="text/event-stream")


@stream.get("/text-image")
async def send_stream_text():
    return StreamingResponse(Service().send_stream_text_image(),
                             media_type="text/event-stream")
