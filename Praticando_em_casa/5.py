#Estrutura de decisão - Questão 5:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Aprovado.')
elif media == 10:
    print('Aprovado com Distinção.')
else:
    print('Reprovado.')
    