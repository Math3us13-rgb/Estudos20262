#Estrutura de decisão - Questão 4

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media > 9 or media == 10:
    print('A')
    print('Aprovado.')
elif media > 7.5 or media <= 9:
    print('B')
    print('Aprovado.')
elif media > 6 or media <= 7.5:
    print('C')
    print('Aprovado.')
elif media > 4 or media <= 6:
    print('D')
    print('Reprovado.')
elif media > 0 or media < 4:
    print('E')
    print('Reprovado.')