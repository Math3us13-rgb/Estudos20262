#Atividade 2 - Dia 4
N1 = float(input ('Digite a primeira nota: '))
N2 = float(input ('Digite a segunda nota: '))
N3 = float(input ('Digite a terceira nota: '))
M = (N1 + N2 + N3) / 3

if M < 7:
    print('Que pena, você fará prova final!')
else:
    print('Excelente, você tá livre da prova final!')
F = float(input ('Digite sua nota final: '))
if F >= 5:
    print('Parabéns! Você foi aprovado!')
else:
    print('Que pena, você foi reprovado!')