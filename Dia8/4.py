#Estrutura de decisão - Questão 6

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um último número: '))

if n1 > n2 and n2 > n3:
    print(n1, 'é o maior número.')
elif n2 > n1 and n1 > n3:
    print(n2, 'é o maior número.')
elif n3 > n1 and n1 > n3:
    print(n3, 'é o maior número.')
else:
    print(n1,',',n2,'e',n3, 'são iguais.')