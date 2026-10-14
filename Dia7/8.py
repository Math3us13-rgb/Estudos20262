#Estrutura de decisão: Questão 27

kg1 = int(input('Digite a quantidade em Kg de morangos comprados: '))
kg2 = int(input('Digite a quantidade em Kg de maçãs compradas: '))

if kg1 <= 5:
    pr1 = kg1 * 2.5
else:
    pr1 = kg1 * 2.2
if kg2 <= 5:
    pr2 = kg2 * 1,8
else:
    pr2 = kg2 * 1.5

total = pr1 + pr2
print('Você vai pagar no total:', total)

if kg1 + kg2 > 8 or total > 25:
    total = total * 0.9

print('você vai pagar no total:', total)