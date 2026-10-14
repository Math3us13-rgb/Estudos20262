#Estrutura de decisão: Questão 17

ano = int(input('Digite um número: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')