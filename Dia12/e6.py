#Desenvolva um algoritmo em Python que verifique o menor número de uma
#sequência de números informados pelo usuário. A quantidade de números
#deve ser informada pelo usuário no início o código.

menor = 9999999999999
qtde = int(input('Quantos números? '))

for i in range (qtde):
    numero = int(input('Digite um número: '))
    if numero < menor:
        menor = numero

print(f'O menor número digitado foi {menor}')