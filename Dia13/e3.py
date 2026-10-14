#Desenvolva um algoritmo que leia alturas dos alunos de uma sala de 43
#alunos e verifique quem é o mais alto, o menor e a média de altura.

maior = 0
menor = 999
soma = 0
for pessoa in range(43):
    nome = input('Qual é o seu nome? ')
    alt = float(input('Qual sua altura? '))
    if alt > maior:
        nome_maior = alt
    if alt < menor:
        nome_menor = alt
    soma = soma + alt

media = soma / 43