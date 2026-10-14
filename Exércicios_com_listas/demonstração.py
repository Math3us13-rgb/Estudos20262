#pessoas = ['a', 'b', 'c', 'd']
#aux = pessoas[0]
#pessoas[0] = pessoas[2]
#pessoas[2] = aux
#print(pessoas)

#atualizar um elemento

so = ['xp','7','vista','8','10','11']
campo = input('Qual so vc quer mudar? ')
ind = -1
for i in range(len(so)):
    if so[i] == campo:
        ind = i

if ind == -1:
    print('O SO digitado não está presente na lista.')
else:
    novo = input('Digite o SO que vai substituir: ')
    so[ind] = novo
    print(so)