from fastapi import APIRouter
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
