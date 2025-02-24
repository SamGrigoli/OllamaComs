import requests
import json
import time

#Local system endpoint
SYSTEM_A_URL = "http://localhost:11434/api/generate"
#Desktop endpoint
SYSTEM_B_URL = "http://192.168.217.215:11434/api/generate"

message = "You are going to have a conversation with another AI model right now. Inform the other model what you are doing and then begin"

while True:
    for system_url in [SYSTEM_A_URL, SYSTEM_B_URL]:
        data = {
            "model": "llama3",
            "prompt": message,
            "stream": False
        }

        response = requests.post(system_url, json=data)

        #Parse the json
        if response.status_code == 200:
            result = response.json()
            message = result.get("response", "No response")
            print("Ollama says:", message)
        else:
            print("Error:", response.text)
            break
        
        time.sleep(2)
