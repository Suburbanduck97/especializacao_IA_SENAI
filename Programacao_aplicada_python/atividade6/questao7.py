import json
from pathlib import Path

path = Path('C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade6')
complete_path = path / 'database_q4.json'

def verificar(texto):
    # para juntar as palavras
    mensagem = "".join(texto.split())

    mapear = {
        'oi':'saudation',
        'comovocêfunciona?':'explication',
    }

    saida = ['sair']

    if mensagem in saida:
        return 'sair'
    else:
        return mapear.get(texto, False)

with open (complete_path, 'r', encoding='utf-8') as arq:
    resposta = json.load(arq)

while True:
    mensagem = input('Digite alguma coisa: ').lower().strip(' ')
    validacao = verificar(mensagem)

    if validacao == 'sair':
        print('Chatbot encerrado!')
        break
    
    if validacao:
        print('\nResposta:')
        print(resposta['response'][validacao])
        print()
    else:
        print()
        print('Não compreendi!')
        print()
    
    