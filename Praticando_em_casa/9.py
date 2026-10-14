#Estrutura de decisão - Questão 9:

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

if (n1 > n2) and (n2 > n3):
    print(n1, n2, n3)
elif (n2 > n3) and (n3 > n1):
    print(n2, n3, n1)
else:
    print(n3, n1, n2)