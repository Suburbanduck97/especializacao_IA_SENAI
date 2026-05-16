import json
from pathlib import Path

path = Path('C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade6')
complete_path = path / 'database_q1.json'

def verificar_entrada(message):
    mapping = {
        'carrinho':'cart',
        'compras':'shopping',
        'compra':'shopping',
        'devolucao':'devolution',
        'devolução':'devolution',
        'endereco':'address',
        'endereço':'address',
        'entrega':'delivery',
        'entregas':'delivery'
    }

    out = ['encerrar', 'finalizar', 'nao', 'não']

    if message in out:
        return 'end'
    return mapping.get(message, False)
  
with open(complete_path, 'r', encoding='utf8') as arq:
    response = json.load(arq)

print('========= Dev`Dor Boot ===========')
print(response['message']['initial'])

while True:
    user_message = input('Digite sua mensagem: ').lower().strip()

    intent = verificar_entrada(user_message)

    if not intent:
        print(response['message']['confused'])
        continue

    if intent == 'end':
        print(response['message']['end'])
        break

    if intent in response['response']:
        print('\nResposta:')
        print(response['response'][intent])
        print(f'\n{response['message']['progress']}')
