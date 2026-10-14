#Estrutura de decisão - Questão 24:
N1 = int(input('digite um número: '))
N2 = int(input('digite um número: '))

O = input('digite o símbolo da operaçao: ')
R = 0
if O == '+':
    R = N1 + N2
if O == '-':
    R = N1 - N2
if O == '*':
    R = N1 * N2
if O == '/':
    R = N1 / N2

if O % 2 == 0:
    print('par')
else:
    print('ímpar')

if R > 0:
    print('positivo')
if R < 0:
    print('negativo')

if R % 1 == 0:
    print('inteiro')
else:
    print('decimal')