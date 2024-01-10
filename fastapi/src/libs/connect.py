import grpc
import search_pb2
import search_pb2_grpc
from concurrent import futures


class SearchServicer(search_pb2_grpc.SearchServiceServicer):
    def SearchService(self, request, context):
        result = "Search Result for {}: {}".format(request.username, request.content)
        return search_pb2.Result(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    search_pb2_grpc.add_SearchServiceServicer_to_server(SearchServicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
