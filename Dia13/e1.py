#desenvolva um programa que identifique se um número é primo ou não.

qtde = 0
num = int(input('Digite um número: '))
for i in range(2, num):
    if num % i == 0:
        qtde = qtde + 1

if qtde == 0:
    print('É primo.')
else:
    print('Não é primo.')