#remover
profs_top = ['Ludgero','Luciano','Erica','Fernanda','Rene']
#função que remove pelo índice
profs_top.pop(4)

print(profs_top)

op = -1
bandas = []
while op != 0:
    print('___Festival Rock PB___')
    print('1- Cadastrar Banda: ')
    print('2- Remover Bandas: ')
    print('3- Listar Bandas: ')
    op = int(input('Digite a opção desejada: '))
if op == 1:
    cadastro = input('Qual Banda deseja cadastrar? ')
    cadastro.append(cadastro)

elif op == 2:
    remover = input('Qual Banda deseja remover? ')
    if bandas.count(remover) > 0:
        bandas.remove(remover) #remove
        #ou
        bandas.pop(bandas.index(remover)) #pop
    #ou:
    #ind = -1
    #for i in range(len(bandas)):
        #if remover == bandas[i]:
            #ind = i
    #if ind == -1:
        #print('Banda não encontrada.')
    #else:
        #bandas.pop(ind) #pop remove pelo índice.
        #print('anda removida com sucesso.')