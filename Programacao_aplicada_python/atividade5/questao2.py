import requests

url = 'https://api.github.com'

try:
    response = requests.get(url)
    dados = response.json()
except requests.HTTPError as e:
    print(e)
    
print(dados)