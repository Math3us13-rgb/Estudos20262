#Estrutura de repetição - Questão 7:

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
n4 = float(input('Digite outro número: '))
n5 = float(input('Digite outro número: '))

while (n1 > n2) and (n2 > n3) and (n3 > n4) and (n4 > n5):
    print(n1)
while (n2 > n1) and (n1 > n3) and (n3 > n4) and (n4 > n5):
    print(n2)
while (n3 > n1) and (n1 > n2) and (n2 > n4) and (n4 > n5):
    print(n3)
while (n4 > n1) and (n1 > n2) and (n2 > n3) and (n3 > n5):
    print(n4)
while (n5 > n1) and (n1 > n2) and (n2 > n3) and (n3 > n4):
    print(n5)
else:
    print('Empate.')