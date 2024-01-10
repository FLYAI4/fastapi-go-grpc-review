import grpc
from .schema import SearchPayload
from libs.exception import UserError
from generated.search_pb2 import Search
from generated.search_pb2_grpc import SearchServiceStub


class UserService:

    def search_openai(self, payload: SearchPayload) -> str:
        if not payload:
            raise UserError(400, "No contents!!")

        resp = ""
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = SearchServiceStub(channel)

            request = Search(
                username=payload.username,
                content=payload.content)
            resp = stub.RequestSearch(request)

        return resp
