#continue
#Quando acionado dentro do laço,remete diretamente para o início
#da repetição.

qtde = 0
nome = ''
while nome != 'fim':
    nome = input('Digite seu nome ou digite fim para encerrar: ')
    if nome == 'Rafael':
        continue
    qtde = qtde + 1
    if nome == 'fim':
        qtde = qtde - 1
        break

print('A quantidade final foi de:', qtde)

#ou:
#while nome True:
    #nome = input('Digite seu nome ou digite fim para encerrar: ')
    #if nome == 'Rafael':
        #continue
    #if nome == 'fim':
        #break
    #qtde = qtde + 1