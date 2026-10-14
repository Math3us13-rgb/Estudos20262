#Desenvolva um algoritmo que leia a idade de uma pessoa e informe para
#ela se ela está fora dos parâmetros de normalidade para entrar na PF.
#A PF aceita apenas pessoas de 18 até 34.

i = int(input('Digite sua idade: '))
if i < 18 or i > 34:
    print('Sinto muito, você não está dentro dos parâmetros para entrar na PF.')
else:
    print('Parabéns, você está dentro dos parâmetros para entrar na PF.')