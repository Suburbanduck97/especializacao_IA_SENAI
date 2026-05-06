class Aluno():
    def __init__(self, nome, nota1, nota2):
        self._nome = nome
        self._nota1 = nota1
        self._nota2 = nota2

    
    def get_nome(self):
        return self._nome

    def calcular_media(self):
        return (self._nota1 + self._nota2) / 2


print('Cadastre seu aluno e veja a média das notas dele')
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a NOTA 1 do aluno: '))
nota2 = float(input('Digite a NOTA 2 do aluno: '))

aluno = Aluno(nome=nome, nota1=nota1, nota2=nota2)
media = aluno.calcular_media()
print(f'A média de {aluno.get_nome()} é {media: .1f}')