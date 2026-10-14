#o professor de Cálculo 1, Flavio, pediu para você construir um
#algoritmo em Python para receber do usuário os 3 lados de um triângulo.
#um programa deve informar se o triângulo é equilátero ou não.

L1 = float(input('Digite o valor do primeiro lado: '))
L2 = float(input('Digite o valor do segundo lado: '))
L3 = float(input('Digite o valor do terceiro lado: '))

if L1 == L2 and L2 == L3:
    print('Excelente! É um triângulo equilátero!')
else:
    print('Que pena, isso não é um triângulo equilátero...')