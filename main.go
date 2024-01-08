package main

import (
	"fmt"

	"github.com/robert-min/fastapi-go-grpc-review/api"
)

func main() {
	resp := api.GetOpenai("")
	fmt.Println(resp)
}
