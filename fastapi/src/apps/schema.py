import pydantic


class SearchPayload(pydantic.BaseModel):
    username: str
    content: str
