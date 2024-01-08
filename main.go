package main

import (
	"fmt"

	"github.com/robert-min/fastapi-go-grpc-review/lib"
)

func main() {
	token, err := lib.GetOpenaiToken()
	if err != nil {
		fmt.Println("Error : ", err)
	}

	fmt.Println(token)
}
