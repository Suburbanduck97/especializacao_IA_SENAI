from pathlib import Path
import requests
import json

path = Path('C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade5')
complete_path = path / 'dados_api.json'

def salve_json(arg_json):
    with open(complete_path, 'w', encoding='utf-8') as arq:
        json.dump(arg_json, arq, indent=4)
        return 'Sucessful! Json Salved.'
    
    return 'Error! Json Don`t Salved.'

try:
    response = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=35217e29')
    response.raise_for_status()
    data_json = response.json()
    print(salve_json(data_json))
except Exception as e:
    print(f'Error: {e}')
