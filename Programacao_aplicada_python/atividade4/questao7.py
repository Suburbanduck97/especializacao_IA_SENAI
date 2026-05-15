PATH = 'C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade4'
COMPLETE_NAME = PATH/'tarefas.txt'

def datasave(task):
    with open(COMPLETE_NAME, 'a', encoding='utf-8') as arquive:
        arquive.write(task)
        arquive.write('\n')
    
    print('Saved Message!')

for i in range(3):
    task = input(f'Digite a {i+1}ª tarefa: ')
    datasave(task)