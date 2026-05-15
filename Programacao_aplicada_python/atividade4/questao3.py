PATH = 'C:\\Users\\erics\\Downloads\\codigos\\Especializacao-IA-SENAI\\Programacao_aplicada_python\\atividade4'
COMPLETE_NAME = {PATH}/'notas.txt'

def verify_data(nota):
    try:
        nota = float(nota)
        if nota < 0 or nota > 10:
            print('Notas Inválidas, Digite uma nota entre 0 e 10.0!')
            return False
        return True
    except ValueError:
        print('Digite notas válidas!')
        return False


def datasave(nota):
    with open(COMPLETE_NAME, 'a', encoding='utf-8') as arquive:
        arquive.write(nota)
        arquive.write('\n')
    
    print('Saved notas!')

while True:
    for i in range(2):
        while True:
            nota = input(f'Digite a {i+1}ª notas: ')
            if verify_data(nota):
                datasave(nota)
                break
            else:
                print('Tente novamente.')      
    break

