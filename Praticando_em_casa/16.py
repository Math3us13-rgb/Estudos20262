#Estrutura de decisão - Questão 16:

valorA = float(input('Digite o valor de A: '))

if valorA <= 0:
    print('Esta equação não é de 2° grau.')

elif valorA != 0:
    valorB = float(input('Digite o valor de B: '))
    valorC = float(input('Digite o valor de C: '))

delta = (valorB ** 2) - (4 * valorA * valorC)

if delta < 0:
    print('O valor de Delta é', delta, 'a equação não possui valores reais.')
elif delta == 0:
    raiz_1 = (-valorB + delta) / (2 * valorA)
    raiz_2 = (-valorB - delta) / (2 * valorA)
print('delta é positivo. A equação possui 2 raízes reais:')
print(f"Raiz 1 = {raiz_1}")
print(f"Raiz 2 = {raiz_2}")