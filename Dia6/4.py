#Atividade da lista de decisão - Questão 11:

S = float(input('Digite o salário do colaborador: '))

if S <= 280:
    A = 0.2
if S > 280 and S <= 700:
    A = 0.15
if S > 700 and S <= 1500:
    A = 0.1
if S > 1500:
    A = 0.05

V = S * A
F = S + V

print('Antes ele recebia:', S)
print('Mas ele ganhou um aumento de', A * 100, 'porcento')
print('Isso fez o salário dele aumentar', V)
print('Sendo assim, no final ele ganhará,', F)