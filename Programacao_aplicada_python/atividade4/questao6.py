PATH = 'C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade4'
COMPLETE_NAME = {PATH}/'respostas.txt'

def datasave(response):
    with open(COMPLETE_NAME, 'a', encoding='utf-8') as arquive:
        arquive.write(response)
        arquive.write('\n')
    
    print('Saved Message!')

response = input('Digite uma menssagem: ')
datasave(response)