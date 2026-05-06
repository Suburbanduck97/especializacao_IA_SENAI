def e_numerico(numero):
    try:
        return float(numero) 
    except ValueError:
        return False
    

while(True):
    valor = input('Digite um valor qualquer: ')
    
    if not e_numerico(valor):
        print('Digite somente valores numéricos!')
        continue

    break

resultado = e_numerico(valor)

if resultado > 0:
    print(f'{resultado: .1f} É positivo!')
elif resultado == 0:
    print(f'{resultado: .1f} É neutro!')
else:
    print(f'{resultado: .1f} É negativo!')


