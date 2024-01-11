import grpc
from .schema import SearchPayload
from libs.exception import UserError
import generated.search_pb2 as search_pb2
import generated.search_pb2_grpc as search_pb2_grpc


class UserService:

    def search_openai(self, payload: SearchPayload) -> str:
        if not payload:
            raise UserError(400, "No contents!!")
        
        resp = ""
        with grpc.insecure_channel('localhost:5051') as channel:
            stub = search_pb2_grpc.SearchServiceStub(channel)

            request = search_pb2.Search(
                username=payload.username,
                content=payload.content)
            resp = stub.RequestSearch(request)
            print(resp.result)

        return resp
