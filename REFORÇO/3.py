#Estrutura de Decisão - Revisando a questão 14:

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
conceito = ""

if media > 9.0:
    conceito = "A"
if media <= 9 and media >= 7.5:
    conceito = "B"
if media >= 6.5 and media <= 7.5:
    conceito = "C"
if media >= 4 and media >= 6:
    conceito = "D"
if media <= 4 and media == 0:
    conceito = "E"

else;
    print('Nota invalida')

if media == 'A' and media == 'B' and media == 'C':
    print('APROVADO!')

else:
    print('REPROVADO!')