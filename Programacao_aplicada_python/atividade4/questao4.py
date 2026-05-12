PATH = '\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python'
COMPLETE_NAME = f'{PATH}\\chatbot.txt'

def restored_chat():
    with open (COMPLETE_NAME, 'r', encoding='utf-8') as arquive:
        for line in arquive:
            print(line.strip())

print('Histórico de Mensagens:')
restored_chat()