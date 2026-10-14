#Atividade da lista de decisão - Questão 16:

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a == 0:
    print('Não é uma equação de segundo grau.')
else:
    delta = (b * b) * 4 * a * c
    if delta < 0:
        print('Não possui raízes reais.')
    if delta == 0:
        x = (-b + delta ** (1/2)) / (2 * a)
        print('Esta é a raiz real:', x)
    if delta > 0:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print('Raiz real positivo:', x1)
        print('Raiz real negativo:', x2)