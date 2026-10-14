#Estrutura de decisão - Questão 8:

p1 = float(input('Digite o valor deste produto:'))
p2 = float(input('Digite o valor deste produto:'))
p3 = float(input('Digite o valor deste produto:'))

if (p1 > p2) and (p2 > p3):
    print('O 3° produto vale mais por custar apenas', p3, 'R$')
elif (p2 > p3) and (p3 > p1):
    print('O 1° produto vale mais por custar apenas', p1, 'R$')
else:
    print('O 2° produto vale mais por custar apenas', p2, 'R$')