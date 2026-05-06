def gerar_tabuada(numero):
    for i in range(11):
        print(f'{numero} x {i} = {i*numero}')

numero = int(input('Digite um número inteiro qualquer: '))
gerar_tabuada(numero)