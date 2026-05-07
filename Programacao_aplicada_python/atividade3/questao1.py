def sugerir_filmes(filmes, categoria):
    categoria = categoria.strip().lower().title()

    for filme in filmes:
        if categoria in filme['categoria']:
            return filme
    
    return 'Categoria não encontrada na base de dados!'


filmes = [
    {
        'nome':'O Senhor dos Anéis: A Sociedade do Anel',
        'categoria': ['Fantasia', 'Ação'],
        'ano':'2001'
    },
    {
        'nome':'Um Estranho no Ninho',
        'categoria': ['Drama', 'Psicológico'],
        'ano':'1975'
    },
    {
        'nome':'Cisne Negro',
        'categoria': ['Suspense', 'Drama'],
        'ano':'2010'
    }
]

categoria = input('Digite uma categoria de filme qualquer: ')
response = sugerir_filmes(filmes, categoria)
print(response)