import json
from pathlib import Path

path = Path('C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade6')
complete_path = path / 'database_q2.json'

def word_validation(word):
    mapping = {
        'bom':'positive',
        'good':'positive',
        'gostei':'positive',
        'adorei':'positive',
        'ótimo':'positive',
        'otimo':'positive',
        'legal':'positive',
        'ruim':'negative',
        'pessimo':'negative',
        'pessímo':'negative',
        'chato':'negative',
        'horrivel':'negative',
        'horrível':'negative',
    }

    return mapping.get(word, False)

with open(complete_path, 'r', encoding='utf-8') as arq:
    response = json.load(arq)

word = input('Digite uma palavra avaliativa: ').lower().strip()
intent = word_validation(word)

if intent:
    print(response[intent])
else:
    print('Não é possível classificar essa avaliação.')