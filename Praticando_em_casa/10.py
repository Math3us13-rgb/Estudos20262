#Estrutura de decisão - Questão 10:

print('Responda a seguinte questão com uma das seguintes alternativas:'
      'M-matutino, V-vespertino ou N-noturno.')
turno = input('Em que turno você estuda? ')
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Digite uma das 3 alternativas mencionadas inicialmente.')