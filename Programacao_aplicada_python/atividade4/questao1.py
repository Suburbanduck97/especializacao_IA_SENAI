PATH = '\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python'
COMPLETE_NAME = f'{PATH}\\aula1data.txt'

def datasave(username):
    with open(COMPLETE_NAME, 'w', encoding='utf-8') as arquive:
        arquive.write(username)
    
    print('Username Saved!')
    

userame = input('Digite Seu nome de usuário: ')
datasave(userame)
