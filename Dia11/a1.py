#Estrutura de Repetição - Questão 1

nota = float(input('Digite uma nota entre 0 a 10: '))

while nota < 0 or nota > 10:
    print('Nota invalida, digite novamente entre 0 a 10:')
    nota = float(input('Digite uma nota entre 0 a 10: '))

print('nota válida informada, ', nota)