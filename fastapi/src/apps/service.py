import grpc
from .schema import SearchPayload
from libs.exception import UserError
import pbs.search_pb2 as search_pb2
import pbs.search_pb2_grpc as search_pb2_grpc

gRPC_SERVER_ADDRESS = "localhost:50051"


class UserService:

    def search_openai(self, payload: SearchPayload) -> str:
        if not payload:
            raise UserError(400, "No contents!!")

        response = ""
        with grpc.insecure_channel(gRPC_SERVER_ADDRESS) as channel:
            stub = search_pb2_grpc.SearchServiceStub(channel)

            request = search_pb2.Request(
                username=payload.username,
                content=payload.content)
            response = stub.ProcessSearch(request)
            # print(response.result)

        return response.result
