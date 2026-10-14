#questão 7
f = int (input ('Quantas fatias de pizza existem no total?'))
a = int (input ('Quantos amigos vão comer?'))
r = f // a
s = f % a
print('Cada amigo receberá', r, 'fatias de pizza!')
print('Em contra partida, sobrou', s, 'fatias')