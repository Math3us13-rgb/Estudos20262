#Estrutura de Repetição - Questão 5:

continuar = True
while continuar:
    populacao_a = int(input('Digite o número da população do País A: '))
    populacao_b = int(input('Digite o número da população do País B: '))

crescimento_a = float(input('Digite o valor do crescimento da população de A: '))
crescimento_b = float(input('Digite o valor do crescimento da população de B: '))
anos = 0

while True:
    anos += 1
    populacao_a *= 1 + (crescimento_a / 100)
    populacao_b *= 1 + (crescimento_b / 100)

    if populacao_a > populacao_b:
        print('Levou', anos, 'para a população A passar ou igualar a B.')
        print('A tem', populacao_a, 'de habitantes.')
        print('B tem', populacao_b, 'de habitantes.')

    continuar = True if input("Deseja continuar (S/N)? > ").upper() == "S" else False