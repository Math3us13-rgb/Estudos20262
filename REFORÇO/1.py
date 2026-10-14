#Estrutura de Decisão - Revisando a questão 11:

s = float(input('Digite seu salário: '))

if s <= 280:
    a = 0.20
if s >= 280 and s <= 700:
    a = 0.15
if s >= 700 and s <= 1500:
    a = 0.10
if s > 1500:
    a = 0.05
v = s * a
f = s + v

print('Antes, você recebia R$', s)
print('Mas com o aumento de', a * 100, 'porcento')
print('Isso faz seu salário aumentar.', v)
print('Sendo assim, no fim, você ganhará R$', f)