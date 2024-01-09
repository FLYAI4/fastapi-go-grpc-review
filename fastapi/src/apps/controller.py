from fastapi import APIRouter
from .schema import SearchPayload
from .service import UserService

search = APIRouter(prefix="/search")


@search.post("/openai")
async def search_openai(
    payload: SearchPayload,
):
    resp = UserService.search_openai(payload)
    return resp
