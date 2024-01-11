package app

import (
	"context"
	"fmt"
	"log"
	"net"

	"github.com/robert-min/fastapi-go-grpc-review/api"
	"github.com/robert-min/fastapi-go-grpc-review/pb"
	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedSearchServiceServer
}

// ProcessSearch make response with requesting Openai API
func (s *server) ProcessSearch(ctx context.Context, req *pb.Request) (*pb.Response, error) {
	log.Printf("Recived request from API server: %s", req.Username)

	result := api.GetOpenai(req.Content)
	response := &pb.Response{Result: fmt.Sprintf("OpenAI response : %s", result)}
	return response, nil
}

// SearchRequest connect gRPC
func SearchRequest() {
	lis, err := net.Listen("tcp", "localhost:50051")
	if err != nil {
		log.Fatalf("Failed to connect: %v", err)
		return
	}

	grpcServer := grpc.NewServer()
	pb.RegisterSearchServiceServer(grpcServer, &server{})

	fmt.Println("Server is listening on port 50051...")
	if err := grpcServer.Serve(lis); err != nil {
		fmt.Println("Failed to serve:", err)
	}
}
