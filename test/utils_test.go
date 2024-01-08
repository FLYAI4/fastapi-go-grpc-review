package test

import (
	"testing"

	"github.com/robert-min/fastapi-go-grpc-review/lib"
	"github.com/stretchr/testify/assert"
)

// TestReadYaml is not valid test case
// TODO: "go test" is not accept relative path. Find other case.
func TestReadYaml(t *testing.T) {
	token, err := lib.GetOpenaiToken()
	if err != nil {
		t.Fatalf("Expeted non-nil error, got: %v", err)
	}
	assert.Equal(t, token, "test-token-1234", "Not valid config")
}
