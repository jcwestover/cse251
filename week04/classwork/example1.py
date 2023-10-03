import requests

request = requests.get(r'http://127.0.0.1:8790/')

response = request.json()
print(f'{response=}')
print(f'{response["films"]}')
sixth_film = f'{response["films"]}' + "6"
response = requests.get(sixth_film)
print(f'sixth film = {response.json()}')