notas = []
for i in range(5):
   nota = float(input(f'Digite a {i+1}ª nota: '))
   notas.append(nota)

media = sum(notas) / len(notas)

if media >= 6:
   print('Aprovado')
else:
   print('Reprovado!')