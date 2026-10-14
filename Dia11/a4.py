#Estrutura de repetição - Questão 4:

populacao_a = 80.000
populacao_b = 200.000
anos = 0

while True:
    anos += 1
    populacao_a += 1 + (3/100)
    populacao_b += 1 + (1.5/100)
    if populacao_a > populacao_b:
        print('Levou', anos, 'para o País A passar ou igualar a população do país B.')
        print('Agora, população do País A é de', populacao_a, 'e do País B é de', populacao_b, '.')