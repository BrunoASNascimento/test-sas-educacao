import requests
import json
from pathlib import Path


url = "https://us-central1-weather-1-a2ea6.cloudfunctions.net/test_input_data_json"

payload = input(
    'Por favor, insira um valor json, ou o caminho de um arquivo json que você deseje enviar: ')

if payload.endswith('.json') or payload.endswith('.txt'):
    file_name = Path(payload)
    with open(file_name, 'r', encoding='utf-8') as file:
        file_value = file.read()
        payload = json.loads(file_value)

else:
    payload = json.loads(payload)


headers = {
    'Authorization': f"Bearer {input('Por favor, insira a chave de segurança: ')}",
    'Content-Type': 'application/json'
}

response = requests.request(
    "POST",
    url,
    headers=headers,
    data=json.dumps(payload).encode('utf-8')
)

print(response.status_code)
print(response.text)
