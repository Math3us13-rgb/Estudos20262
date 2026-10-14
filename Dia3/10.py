#Porcentagens - Questão 2
v = float (input ('Digite o valor de um produto: '))
d = float (input ('Agora, digite o valor do desconto ganho pelo cliente:'))
f = v - (v * (d / 100))
print('O valor final a ser pago pelo cliente deverá ser de R$', f)