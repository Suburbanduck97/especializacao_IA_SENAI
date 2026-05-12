PATH = '\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python'
COMPLETE_NAME = f'{PATH}\\chatbot.txt'

def datasave(message):
    with open(COMPLETE_NAME, 'a', encoding='utf-8') as arquive:
        arquive.write(message)
        arquive.write('\n')
    
    print('Saved Message!')

message_text = input('Digite uma menssagem: ')
datasave(message_text)