module github.com/robert-min/fastapi-go-grpc-review

go 1.20

replace github.com/robert-min/fastapi-go-grpc-review/lib => ./lib

replace github.com/robert-min/fastapi-go-grpc-review/api => ./api

require (
	github.com/stretchr/testify v1.8.4
	gopkg.in/yaml.v3 v3.0.1
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/sashabaranov/go-openai v1.17.10 // indirect
)
