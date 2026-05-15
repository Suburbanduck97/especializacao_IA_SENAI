import requests
import json

url = 'https://restcountries.com/v3.1/name/brazil'
try:
    response = requests.get(url)
    response.raise_for_status()
    data_response = response.json()
    data_dict = data_response[0]
    json_response = {
        'country_name':data_dict['name']['nativeName']['por']['common'],
        'capital':data_dict['capital'][0],
        'population':data_dict['population']
    }
    system_response = json.dumps(json_response, indent=3, ensure_ascii=False)
    print(system_response)

except Exception as e:
    print(f'Erro ao consultar: {e}')

# json.dumps => De Dicionário para Json
# json.loads => De Json para dicionário