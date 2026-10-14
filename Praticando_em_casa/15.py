#Estrutura de decisão - Questão 15:

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if lado1 == lado2 and lado2 == lado3:
    print('Este é um triangulo equilátero.')
elif lado1 != lado2 and lado2 != lado3:
    print('Este é um triangulo escaleno.')
else:
    print('Este é um triangulo isoceles.')