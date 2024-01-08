package lib

import (
	"log"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestReadConfigFile(t *testing.T) {
	// 1.조건 : 유효한 yaml 파일 생성
	tempFile, err := os.CreateTemp("", "test_config_*.yaml")
	if err != nil {
		log.Fatalf("임시 파일 생성 중 오류 발생: %v", err)
	}
	defer os.Remove(tempFile.Name()) // 테스트 종료 후 파일 삭제

	// 테스트용 구성 파일 데이터 작성
	testConfigData := []byte(`
test:
  token: test-token-1234
openai:
  token: s12312312314
`)
	// 테스트용 구성 파일에 데이터 작성
	err = os.WriteFile(tempFile.Name(), testConfigData, 0644)
	if err != nil {
		log.Fatalf("테스트용 구성 파일에 데이터 쓰기 중 오류 발생: %v", err)
	}

	// 2. 수행 : file load
	config, err := readConfigFile(tempFile.Name())
	if err != nil {
		t.Fatalf("Expeted non-nil error, got: %v", err)
	}

	// 3. 기대하는 결과 : 파일에 있는 값과 동일
	assert.Equal(t, config.Test.Token, "test-token-1234", "Not valid config")
}
