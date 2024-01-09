from .schema import SearchPayload
from libs.exception import UserError


class UserService:

    def search_openai(self, payload: SearchPayload) -> str:
        if not payload:
            raise UserError(400, "No contents!!")

        # TODO : gRPC 요청
        return payload.content
