#Break
#É um comando usado pra encerrar o laço de repetição.
#Funciona em qualquer estrutura de repetição.

resposta = 'não'

while resposta != 'sim':
    resposta = input('Você aceita namorar comigo? ')
    if resposta == 'É o jeito':
        print('Eu que não quero mais.')
        break