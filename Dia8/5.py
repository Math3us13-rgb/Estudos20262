#faça um algoritmo em Python que verifique se o nome digitado pelo
#usuário corresponde a uma das seguintes opções: ruim, bom, ótimo
#para as seguintes perguntas.
#Você gostou das aulas de Algoritmos?
#Você gostou das aulas de Calculo 1?
#Você gostou das aulas de Aoc?
#Você gostou das aulas de Inglês?
#Você gostou das aulas de Português?

#O sistema deve verificar qual a nota média que o aluno deu para o
#semestre letivo.

print('Responda as seguintes questões com: ruim, bom ou ótimo.')

p1 = input('Você gostou das aulas de Algoritmos? ')
p2 = input('Você gostou das aulas de Calculo 1? ')
p3 = input('Você gostou das aulas de Aoc? ')
p4 = input('Você gostou das aulas de Inglês? ')
p5 = input('Você gostou das aulas de Português? ')

soma = 0
if p1 == 'ruim':
    soma = soma + 5

elif p1 == 'bom':
    soma = soma + 7

elif p1 == 'ótimo':
    soma = soma + 10

elif p2 == 'ruim':
    soma = soma + 5

elif p2 == 'bom':
    soma = soma + 7

elif p2 == 'ótimo':
    soma = soma + 10

elif p3 == 'ruim':
    soma = soma + 5

elif p3 == 'bom':
    soma = soma + 7

elif p3 == 'ótimo':
    soma = soma + 10

elif p4 == 'ruim':
    soma = soma + 5

elif p4 == 'bom':
    soma = soma + 7

elif p4 == 'ótimo':
    soma = soma + 10

elif p5 == 'ruim':
    soma = soma + 5

elif p5 == 'bom':
    soma = soma + 7

else:
    soma = soma + 10

media = soma / 5

print ('a média geral do semestre foi:', media)