#Estrutura de decisão - Questão 14:

nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
media = (nt1 + nt2) / 2

if media >= 9 or media <= 10:
    print('Nota A')
    print('APROVADO')
elif media >= 7.5:
    print('Nota B')
    print('APROVADO')
elif media >= 6:
    print('Nota C')
    print('APROVADO')
elif media >= 4:
    print('Nota D')
    print('REPROVADO')
else:
    print('Nota F')
    print('REPROVADO')