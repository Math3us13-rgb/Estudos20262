adms = ['Master', '123', True]
dentistas = []
pacientes = []
consultas_agendadas = []
consultas_canceladas = []
consultorios = []
lista_pacientes = []
agenda_geral = []

programa = True

while programa:
    print('==========MENU==========' '\nSelecione as seguintes opções'
          'conforme seu cargo'
          '\nVocê é:' '\n1- ADM:' '\n2- Paciente:'
          '\n3- Fechar programa:')
    res = input('Selecione a opção desejada: ')

    if res == '1':
        print('==========MENU==========' '\nSelecione as seguintes informações:'
              '\n1-Logar na conta:' '\n2- Cadastrar conta:' '\n3- Voltar ao menu principal:')
        res1 = input('Selecione a opção desejada: ')
        if res1 == '1':
            print('')
        elif res1 == '2':
            print('')

    if res == '2':
        while True:
            print('==========MENU==========' '\nDigite as seguintes'
            'informações:' '\n1- Digite CPF:' '\n2- Cadastrar CPF:'
            '\n3- Voltar ao menor principal: ')
            res2 = input('Selecione a opção desejada: ')
            if res2 == '1':
                print('')
            elif res2 == '2':
                print('Cadastre as seguintes informações:')
            nome = input('Informe seu nome: ')
            cpf = input('Informe seu CPF: ')
            senha = input('Informe seu senha: ')
            telefone = input('Informe seu telefone: ')
            novo_paciente = [nome, cpf, senha, telefone]
            print('Informações cadastradas com sucesso!')
            pacientes.append(novo_paciente)


    else:
        print('Opção inválida! Tente novamente!\n')

    if res == '3':
        print('Fechando o programa...')
        print('Programa fechado.')
        break