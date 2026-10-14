#Desenvolva um algoritmo em Python e faça a leitura do número dos
#candidatos (99,88). Leia a votação para uma turma de 38 alunos.
#Ao final, compute os votos e diga quem ganhou.

v99 = 0
v88 = 0
i = 0

while i < 38:
    voto = int(input('Digite seu voto: '))
    if voto == 99:
        v99 = v99 + 1
    elif voto == 88:
        v88 = v88 + 1

i = i + 1

if v88 > v99:
    print('A chapa do 88 ganhou!')
elif v99 > v88:
    print('A chapa do 99 ganhou!')
else:
    print('Simbora pro segundo turno porque empatou!')