import json
from pathlib import Path

path = Path('C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade6')
complete_path = path / 'database_q3.json'

def recomendar_filme(categoria):
    mapear = {
        'ficcaocientifica':'ficcao_cientifica',
        'ficçãocientifica':'ficcao_cientifica',
        'ficcao':'ficcao_cientifica',
        'ficção':'ficcao_cientifica',
        'drama':'drama',
        'fantasia':'fantasia',
        'terror':'terror',
    }

    return mapear.get(categoria, False)

with open (complete_path, 'r', encoding='utf-8') as arq:
    response = json.load(arq)

categoria = input('Digite uma categoria de filme: ').lower().strip()

recomendacao = recomendar_filme(categoria)

if recomendacao:
    print('\nFilme recomendado:')
    print(response['filmes'][recomendacao])
else:
    print('Não temos nenhuma recomendação para essa categoria!')