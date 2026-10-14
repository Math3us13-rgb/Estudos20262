#O aluno do P1 José Augusto foi tirar a CNH e foi informado que precisa
#ter 18 anos, fazer o teste psicotécnico e ser aprovado na prova de
#direção. Desenvolva um algoritmo na linguagem Python que pergunte
#para o usuário a idade, se ele foi aprovado no psicotécnico e se
#foi aprovado no teste de direção. O programa deve informar se ele
#receberá sim ou não a CNH.

I = int(input('Digite sua idade: '))
P = input('voce foi aprovado no psicotecnico: sim ou nao? ')
D = input('voce foi aprovado no teste de direçao: sim ou nao? ')

if I >= 18:
    if P == 'sim':
        if D == 'sim':
            print('voce pode receber sua CNH')
        else:
            print('poxa, faltou só passar na prova prática de direçao')
    else:
        print('você precisa ter mais atençao no psicotecnico')
else:
    print('aguarde completar 18 anos de idade')