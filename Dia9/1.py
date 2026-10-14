nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Diga seu salário: '))
emprestimo = float(input('Digite o valor do emprestimo desejado: '))
meses = int(input('Em quantos meses você deseja pagar? '))

parcela = emprestimo / meses
limite = salario * 0.32

if (idade >= 18) and (emprestimo <= limite):
    print('Parabéns,', nome, 'seu empréstimo foi aprovado!')
else:
    print('Infelizmente,', nome, 'seu empréstimo foi negado.')