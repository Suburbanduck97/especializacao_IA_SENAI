notas = []
for i in range (3):
    notas.append(float(input(f'Digite a {i+1}ª nota: ')))

media = (sum(notas)/len(notas))

if media >= 9.0:
    print('Desempenho Excelente!')
elif media >= 7.0:
    print('Desempenho Bom!')
elif media >= 5.0:
    print('Desempenho Razoável!')
else:
    print('Desempenho Insuficiente!')
    