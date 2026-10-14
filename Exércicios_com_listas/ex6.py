#Questão 6:

alunos = 10
notas = 4

medias = []
media_7 = 0

for i in range(alunos):
    media = 0
    for j in range(notas):
        media += float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
        media = media / notas
    if media >= 7:
        media_7 += 1

print('\n A média dos alunos formam:')
for i in range(alunos):
    print(f'Nota {i+1}: {medias[i]:.2f}')

print(f"\n{media_7} alunos tiveram média maior ou igual a 7.")