#Construa um alogoritmo em Python que consiga ler 10 números informados
#pelo usuário. O código deve ao final informar a quantidade de números
#pares e ímpares.

contador = 1
par = 0
impar = 0
while contador <= 10:
    num = int(input('Digite um núero: '))
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print('A quantidade de números pares é de:', par)
print('A quantidade de números impares é de:', impar)