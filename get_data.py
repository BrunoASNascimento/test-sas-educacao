import requests
import json

url = "https://us-central1-weather-1-a2ea6.cloudfunctions.net/test_download_data"

payload = "{\r\n    \r\n\r\n    \"value_filter\": [\r\n        0,\r\n        1,\r\n        10\r\n    ],\r\n    \"id_document\": 1\r\n}"


get_type = int(input(
    'Por favor, insira o número da opção que você deseja:\n1- ID do documento\n2- Filtrar documento\nInsira o valor entre 1 e 2: '))
while get_type not in [1, 2]:
    get_type = int(input(
        'Algo deu errado, ´por favor, insira o número da opção que você deseja:\n1- ID do documento\n2- Filtrar documento\nInsira o valor entre 1 e 2: '))


if get_type == 1:
    payload = {
        "id_document": int(
            input('Por favor, insira o ID do documento: ')
        )
    }
elif get_type == 2:
    payload = {
        "name_filter": input('Por favor, insira o nome do filtro que deseja usar: '),
        "value_operator": input('Por favor, insira um dos operadores listado ["<", "<=", "==", ">", ">=", "array-contains", "in"]: '),
        "value_filter": input('Por favor, insira o valor do filtro que deseja usar: ')
    }
    try:
        payload['value_filter'] = eval(payload['value_filter'])
    except:
        pass

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
