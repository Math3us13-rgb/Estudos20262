#faça um algoritmo na linguagem Python que leia os 3 lados
#de um triângulo e verifique se ele é Isoceles ou não:

l1 = float(input('Digite um valor: '))
l2 = float(input('Digite outro valor: '))
l3 = float(input('Digite outro valor: '))

if (l1 == l2 and l2 != l3) or (l1 == l3 and l2 != l3) or (l2 == l3 and l3 != l1):
    print('Isosceles.')
else:
    print('Não é isosceles.')