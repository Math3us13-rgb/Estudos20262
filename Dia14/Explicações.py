#Tipos de dados
#string, float, integer, boolean

#Tipos de estruturas de dados
#lista

lista_amigos = ['Yan', 'Italo','Thamires','Carlos']
#percorrer a lista

busca = input('Digite o nome da pessoa que procura: ')

for amigo in lista_amigos:
    if busca in amigo:
        print('seu amigo está na lista', amigo)

#declarar lista
#inserir na lista
#percorrer/buscar na lista

#percorrer pelo indice:
#todo índice começa pelo zero.

shows_rommel = ['12/10', '25/10', '30/10', '07/11']
#print(shows_rommel[0])
#print(shows_rommel[2])

for ind in range(4):
    print(shows_rommel[ind])