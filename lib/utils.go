package lib

import (
	"os"

	"gopkg.in/yaml.v3"
)

type TestConfig struct {
	Token string `yaml: "token"`
}

type OpenaiConfig struct {
	Token string `yaml: "token"`
}

type Config struct {
	Openai OpenaiConfig `yaml: "openai"`
	Test   TestConfig   `yaml: "test"`
}

func readConfigFile(filePath string) (*Config, error) {
	yamlFile, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}

	var config Config
	err = yaml.Unmarshal(yamlFile, &config)
	if err != nil {
		return nil, err
	}

	return &config, nil
}

// GetOpenaiToken get openai api token.
func GetOpenaiToken() (string, error) {
	config, err := readConfigFile("./lib/config/config.yaml")
	if err != nil {
		return "", err
	}
	return config.Openai.Token, nil
}
