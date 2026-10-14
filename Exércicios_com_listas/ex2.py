#Questão 2:

numeros = []

for i in range (10):
    valor = float(input(f'Digite o {i + 1} número real.'))
    numeros.append(valor)

print('/n Os números na ordem inversa são: ')
for numeros in numeros[::-1]:
    print(numeros)