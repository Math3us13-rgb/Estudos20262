#Lista de decisão: Questão 25
print('Por favor, responda as seguintes questões com "sim" ou "não":')
p1 = input('Você telefonou para a vítima? ').upper()
p2 = input('Você esteve no local do crime? ').upper()
p3 = input('Você mora perto da vítima? ').upper()
p4 = input('Você devia para a vítima? ').upper()
p5 = input('Você trabalhou com a vítima? ').upper()

soma = 0
if p1 == 'sim':
    soma = soma + 1
if p2 == 'sim':
    soma = soma + 1
if p3 == 'sim':
    soma = soma + 1
if p4 == 'sim':
    soma = soma + 1
if p5 == 'sim':
    soma = soma + 1

if soma == 2:
    print('Suspeito.')
if soma == 3 or soma == 4:
    print('Suspeito.')
if soma == 5:
    print('Assassino!')
if soma < 2:
    print('Inocente.')
    
else:
    print('Por favor, digite APENAS "sim" ou "não".')