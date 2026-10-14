print('---Sistema do primeiro ano:---')
alunos = ['Enzo', 'Nycole', 'João Pedro']
print(alunos)
print(alunos[0])
while True:
    print('\n---OPÇÕES:---')
    print('1- Cadastrar aluno: ')
    print('2- Mostrar alunos:')
    print('3- Sair: ')
    op = int(input('Qual a sua opção: '))
    if op == 1:
        nome = input('Qual o nome do aluno?')
        alunos.append(nome)
        print('Pessoa inserida com sucesso!')
    elif op == 2:
        print(alunos)
    elif op == 3:
        break
    print('Opção inválida!')

print('Programa finalizado com sucesso!')