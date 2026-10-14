#Construa um algoritmo que o nome de 150 pessoas e verifique quantas
#possuem maria no nome.

qtde = ''
for qtde in range(150):
    nome = input('Digite o nome: ')
    if 'Maria' in nome:
        qtde = qtde + 1
    if nome.lower() == 'fim':
        break

print(f'Tivemos ao todo {qtde} Marias registradas!')