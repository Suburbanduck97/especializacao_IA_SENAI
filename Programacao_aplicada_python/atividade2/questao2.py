def verificar_paridade(x):
    if x % 2 == 0:
        return True

    return False

numero = int(input('Digite um número qualquer: '))
if verificar_paridade(numero):
    print(f'{numero} é Par')
else:
    print(f'{numero} é ímpar')