#Desenvolva um algoritmo em Python que pergunte para diversos alunos se
#eles estão gostando ou não da disciplina de algortimos (sim ou não).
#O programa deve mostrar quantos votos sim/não tiveram. Se o aluno digitar
#fim. O programa para a leitura e mostra a votação final.

sim = 0
nao = 0
outros = 0
resposta = ''

while resposta != 'fim':
    resposta = input('Você está gostando da disciplina de algoritmos?')
    if resposta == 'sim':
        sim += 1
    elif resposta == 'não':
        nao += 1
    else:
        outros += 1

if sim > nao:
    print('A maioria da sala está gostando de programar.')
elif nao > sim:
    print('Deu ruim. Não tão gostando de programação.')
