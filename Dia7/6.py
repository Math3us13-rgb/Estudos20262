#Desenvolva um algoritmo em Python que leia o valor do litro de alcool
#e o valor do litro de gasolina. O algoritmo deve informar qual
#combustível compensa abastecer.

alc= float(input('Digite o valor do litro do alcool (R$): '))
gas = float(input('Digite o valor do gasolina (R$): '))

if alc/gas < 0.7:
    print('Abasteça com alcool')
else:
    print('Abasteça com gasolina.')