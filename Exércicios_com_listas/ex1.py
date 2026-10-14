#Questão 1:

vetor = []
print('Digite 5 números inteiros: ')
for i in range(5):
    numero = int(input(f"Número {i + 1}: "))
    vetor.append(numero)

print('\n Os números digitados são: ')
print(vetor)