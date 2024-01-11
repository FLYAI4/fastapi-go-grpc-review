package app

import (
	"context"
	"fmt"
	"log"
	"net"

	"github.com/robert-min/fastapi-go-grpc-review/pb"
	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedSearchServiceServer
}

func (s *server) ProcessSearch(ctx context.Context, req *pb.Request) (*pb.Response, error) {
	log.Printf("Recived request from API server: %s", req.Username)

	response := &pb.Response{Result: fmt.Sprintf("Response from Process Server : %s", req.Content)}
	return response, nil
}

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
