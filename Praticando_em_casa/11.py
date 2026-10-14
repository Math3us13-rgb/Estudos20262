#Estrutura de decisão - Questão 11:

salario = float(input('Digite seu salário: '))
R = salario * 1

if salario <= 280:
    R = salario * 0.20
    print('Seu salário agora é de',R, 'R$.')

elif salario >= 280 or salario == 700:
    R = salario * 0.15
    print('Seu salário agora é de',R, 'R$.')

elif salario >= 700 or salario == 1500:
    R = salario * 0.10
    print('Seu salário agora é de', R, 'R$.')

else:
    R = salario * 0.05
    print('Seu salário agora é de ',R, 'R$.')