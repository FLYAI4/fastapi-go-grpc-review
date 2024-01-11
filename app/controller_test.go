package app

import (
	"context"
	"fmt"
	"testing"
	"time"

	"github.com/robert-min/fastapi-go-grpc-review/pb"
	"github.com/stretchr/testify/assert"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const (
	mockContent = "Hellow World!"
)

func TestProcessSearch(t *testing.T) {
	// issue : https://stackoverflow.com/questions/70482508/grpc-withinsecure-is-deprecated-use-insecure-newcredentials-instead
	// go version2.X : grpc.WithInsecure() -> grpc.WithTransportCredentials(insecure.NewCredentials())
	conn, err := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		t.Fatalf("Failed to connect to B server: %v", err)
	}
	defer conn.Close()

	client := pb.NewSearchServiceClient(conn)

	// 1. 조건 : 유효한 요청
	request := &pb.Request{Username: "kim", Content: mockContent}

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	// 2. 수행 : Process에 요청
	response, err := client.ProcessSearch(ctx, request)
	if err != nil {
		t.Fatalf("Error while calling Process server: %v", err)
	}

	// 3. 기대하는 결과 : 응답 동일
	var collectAnswer = fmt.Sprintf("Response from Process Server : %s", mockContent)
	assert.Equal(t, response.Result, collectAnswer, "Not valid config")
}
