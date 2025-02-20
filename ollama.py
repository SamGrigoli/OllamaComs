import requests
import json

#Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

data = {
    "model": "llama3",
    "prompt": "Who was the first elden lord?",
    "stream": False
}

response = requests.post(OLLAMA_URL, json=data)

#Parse the json
if response.status_code == 200:
    result = response.json()
    print("Ollama says:", result["response"])
else:
    print("Error:", response.text)
