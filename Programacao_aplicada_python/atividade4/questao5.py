PATH = '\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python'
COMPLETE_NAME = f'{PATH}\\acessos.txt'

def datasave(username):
    with open(COMPLETE_NAME, 'a', encoding='utf-8') as arquive:
        arquive.write(username)
        arquive.write('\n')
    
    print('Username Saved!')
    

userame = input('Digite Seu nome de usuário: ')
datasave(userame)