#Questão 17:

atletas = []
maior_media = 0
nome_campeao = ''

while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        break
    saltos = list()
    for i in range(5):
        salto = float(input(f'Digite o salto: '))
        media += salto
        saltos.append(salto)
    atletas.append([nome, saltos])
    if media > maior_media:
        maior_media = maior_media
        nome_campeao = nome

print(atletas)