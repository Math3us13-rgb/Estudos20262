#Estrutura de Repetição - Questão 3:

nome = str(input('Digite um nome que contenha mais de 3 caracteres: '))
idade = int(input('Digite uma idade entre 0 a 150: '))
salario = float(input('Digite um salário maior que 0: '))
sexo = input('Digite seu sexo [M/F]: ').lower()
estado_civil = input('Digite seu estado civil [S/C/V/D]: ').lower()

while (len(nome) <= 3):
    print('Nome inválido! Tente novamente.')
    nome = input('Digite um nome que contenha mais de 3 caracteres: ')

while idade < 0 or idade > 150:
    print('Idade inválida! Tente novamente.')
    idade = int(input('Digite uma idade entre 0 a 150: '))

while salario < 0:
    print('Salário inválido! Tente novamente.')
    salario = float(input('Digite um salário maior que 0: '))

while sexo != 'M' or sexo != 'F':
    print('Sexo inválido! Tente novamente.')
    sexo = input('Digite seu sexo [M/F]: ')

while estado_civil != 's' or estado_civil != 'c' or estado_civil != 'v' or estado_civil != 'd':
    print('Estado civil inválido! Tente novamente.')
    estado_civil = input('Digite seu estado civil [S/C/V/D]: ')


    print('todos os dados foram validados com sucesso!')