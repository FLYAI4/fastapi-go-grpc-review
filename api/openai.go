package api

import (
	"context"
	"fmt"

	"github.com/robert-min/fastapi-go-grpc-review/lib"
	openai "github.com/sashabaranov/go-openai"
)

// GetOpenai request the content with openai GPT3.5.
func GetOpenai(content string) string {
	token, err := lib.GetOpenaiToken()
	if err != nil {
		fmt.Println("Error : ", err)
	}
	client := openai.NewClient(token)
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT3Dot5Turbo0301,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: content,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return ""
	}
	return resp.Choices[0].Message.Content
}
