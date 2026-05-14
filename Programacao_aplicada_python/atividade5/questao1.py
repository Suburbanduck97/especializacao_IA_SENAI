import requests

try:
    response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
except requests.HTTPError as e:
    print(e)

dados = response.json()
print(f'{dados['USDBRL']['bid']}')