#Estrutura de decisão - Questão 7:

n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
n3 = float(input('Digite outro valor:'))

if (n1 > n2) and (n2 > n3):
    print(n1, n3)
elif (n2 > n3) and (n3 > n1):
    print(n2, n1)
elif (n1 > n3) and (n3 > n2):
    print(n1, n2)
else: 
    print(n3, n2)