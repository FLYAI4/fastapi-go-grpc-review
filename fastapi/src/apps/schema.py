import pydantic


class SearchPayload(pydantic.BaseModel):
    content: str
