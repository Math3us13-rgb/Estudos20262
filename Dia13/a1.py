#Estrutura de Repetição - Questão 38:

ano_inicial = 1995
sal_inicial = float(input('Quanto você ganha? '))
aumento = 1.5 / 100 #1996
#1997 em diante dobra percentual

for ano in range(1996, 2026):
    sal_ano = sal_inicial * (1 + aumento)
    print(f'No ano de {ano} ele ganha {sal_inicial:.2f}')
    aumento = aumento * 2