#Estrutura de repetição - Questão 2

nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

while senha == nome:
    print('Erro, senha não suportada. Por favor tente novamente.')
    nome = input('Digite seu nome: ')
    senha = float(input('Digite sua senha: '))
