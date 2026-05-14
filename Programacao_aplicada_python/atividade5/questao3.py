import requests
import json

def get_bid(currency):
    url = f'https://economia.awesomeapi.com.br/json/last/{currency}'
    try:
        response = requests.get(url)

        # lança exceção para erros 4... ou 5...
        response.raise_for_status()
        data_dict = response.json()
        currency_data = next(iter(data_dict.values()))
        return currency_data['bid']
       
    except Exception as e:
        return f"Erro ao consultar: {e}"
    

chatbot = [
    {
        'question':'qual valor do dolar hoje?',
        'currency':'USD-BRL',
        'label':'Dólar',
    },
    {
        'question':'qual valor do euro hoje?',
        'currency':'EUR-BRL',
        'label':'Euro',
    },
    {
        'question':'qual valor do bitcoin hoje?',
        'currency':'BTC-BRL',
        'label':'Bitcoin',
    },
]

question_message = input('Pergunte ao chat: ').lower().strip()


found = False
for data in chatbot:
    if data['question'] == question_message:
        bid = get_bid(data['currency'])

        if bid:
            data['response'] = f'Olá, a cotação do {data['label']} hoje é: R${bid}'
        else:
            data['response'] = f'Desculpe, Erro ao acessar o servidor de câmbio'
        
        print(json.dumps(data, indent=4, ensure_ascii=False))
        found = True
        break

if not found:
    print(json.dumps({'error':'Não é possível fornecer esses dados!'}, indent=4, ensure_ascii=False))