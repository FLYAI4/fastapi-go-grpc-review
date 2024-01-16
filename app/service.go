package app

import (
	"fmt"
	"sync"

	"github.com/robert-min/fastapi-go-grpc-review/api"
)

func MakeGoroutine(content string) string {
	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		resp := api.GetOpenai(content)
		fmt.Printf("go func 1 Success : %s \n", resp)
		wg.Done()
	}()

	go func() {
		for i := 1; i < 10; i++ {
			fmt.Println("go func 2 Calling")
		}
		wg.Done()
	}()
	wg.Wait()

	return content
}

func process(wg *sync.WaitGroup, ch chan string) {
	for c := range ch {
		resp := api.GetOpenai(c)
		fmt.Printf("go func channel Success : %s \n", resp)
	}
	wg.Done()
}

func MakeChannel(content string) string {
	var wg sync.WaitGroup

	ch := make(chan string)
	wg.Add(1)

	go process(&wg, ch)

	ch <- content

	close(ch)
	wg.Wait()

	return content
}
