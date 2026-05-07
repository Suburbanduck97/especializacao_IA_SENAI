database = {
    'dados_bons':['bom', 'ótimo', 'otimo', 'legal', 'top'],
    'dados_ruins':['ruim', 'horrível', 'horrivel', 'chato']
}

palavra = input('Digite uma palavra avaliativa: ').lower()

if palavra in database['dados_bons']:
    print('Feedback positivo!')
elif palavra in database['dados_ruins']:
    print('Feedback positivo!')
else:
    print('Feedback neutro!')