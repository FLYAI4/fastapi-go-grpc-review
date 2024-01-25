from fastapi import APIRouter, UploadFile
from .schema import SearchPayload
from .service import UserService
from libs.utils import make_response

search = APIRouter(prefix="/search")


@search.post("/openai")
async def search_openai(
    payload: SearchPayload,
):
    result = UserService().search_openai(payload)
    return make_response(result)


@search.post("/image")
async def post_image(
    file: UploadFile,
):
    return "hello"