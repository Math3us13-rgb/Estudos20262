#operadores lógicos (AND)
curso_online = input ('Você fez curso online? ').upper()
psico = input ('Passou no psicotécnico? ').upper()
toxi = input ('O exame toxicológico apontou algo ilícito?').upper()
pratica = input ('Passou na prática? ').upper()

if curso_online == 'sim' and psico == 'sim' and toxi == 'não' and pratica == 'sim':
    print('Parabéns! Você está apto para tirar a carteira de motorista!')
else:
    print('Que pena, desejo sorte da próxima vez.')