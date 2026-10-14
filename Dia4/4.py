#Atividade 1 - Dia 4
nota = float(input ('Digite a nota que você tirou: '))

if nota > 9:
    #final = nota * 1.1
    final = nota + (nota * 0.1)
    print('Sua nota final foi de:', final)
if nota > 10:
    nota = 10

else:
    print('Sua nota foi de', nota)