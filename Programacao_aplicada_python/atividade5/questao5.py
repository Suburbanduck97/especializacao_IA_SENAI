import json
PATH = 'C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade5\\questao5.json'

with open(PATH, 'r', encoding='utf-8') as arq:
    response = json.load(arq)
    
print(response)