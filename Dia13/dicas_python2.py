#if é uma estrutura de decisão.
#for é uma estrutura de repetição.
#range pode ter 3 parâmetros:
#1- Parâmetro: É o valor inicial
#2- Parâmetro: É a condição de parada
#3- Parâmetro: É o salto que o número faz a cada repetição

#Começa de 0, para em 2026 e aumenta de 1 em 1.
for x in range(2026):
    print(x)
#Começa de 1231, para em 1988 e aumenta de 1 em 1.
for x in range(1231, 1988):
    print(x)
#Começa de 2026, para em 1988 e diminui de 4 em 4.
for x in range (2026, 1988, -4):
    print(x)

#String é um tipo de dado formado por uma cadeia de caracteres.
#len() determina o tamanho de caracteres de uma string.
nome = 'Carlos Henrique Estrela'

for letra in nome:
    print(letra, end= ' ')

#para mostrar apenas as letras em posições impares:
for ind in range(len(nome)):
    if ind % 2 == 0:
    print(nome[ind], end= ' ')

#ler um nome ao contrário:
nome = 'Maria Heloisa Marques'

for ind in range(len(nome) - 1, - 1, - 1):
    print(nome[ind], end= ' ')