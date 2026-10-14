#Questão 3:

notas = []

for i in range(4):
    nota = float(input(f'Digite {i + 1} nota: '))
    notas.append(nota)

media = nota / 4

print('\n A média das notas é:')
print(media)