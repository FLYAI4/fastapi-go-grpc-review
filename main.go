package main

import (
	"fmt"

	"github.com/robert-min/fastapi-go-grpc-review/app"
)

func main() {
	// app.SearchRequest()
	resp := app.MakeChannel("Hello World")
	// resp := api.GetOpenai("")
	fmt.Println(resp)
}
