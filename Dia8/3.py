#desenvolva um algoritmo que verifique se o usuário está elegendo a chapa
#correta para presidente da sala. O algoritmo deve ler o número do voto e
#informar se o usuário votou em algum candidato, se votou nulo ou em
#branco(00). As chapas são: 01, 02, 03, 04.

voto = input('Qual seu voto?')
if voto == '01' or voto == '02' or voto == '03' or voto == '04':
    print('seu voto foi válido.')
elif voto == '00':
    print('seu voto foi em branco.')
else:
    print('seu voto foi invalidado ou nulo.')

    