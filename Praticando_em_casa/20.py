#Estrutura de decisão - Questão 20:

saque = float(input('Digite o valor do saque: '))
nota100 = saque // 100
saque =  saque % 100
nota50 = saque // 50
saque = saque % 50
nota10 = saque // 10
saque = saque % 10
nota5 = saque // 5
saque = saque % 5
nota1 = saque // 1

if saque < 10 or saque < 600:
    print('O valor deve ser de no mínimo 10 reais e no máximo 600.')

print('Saque com notas permitidas: ')

if nota100 > 0:
    print(nota100, 'nota(s) de R$ 100')
elif nota50 > 0:
    print(nota50, 'nota(s) de R$ 50')
elif nota10 > 0:
    print(nota10, 'nota(s) de R$ 10')
elif nota5 > 0:
    print(nota5, 'nota(s) de R$ 5')
elif nota1 > 0:
    print(nota1, 'nota(s) de R$ 1')