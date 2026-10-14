#Operadores lógicos: AND

x = 1
print(x == 2)

nome_professor = 'Renê'
idade_professor = 38
print(nome_professor == 'Renê' and idade_professor == 31)

altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
idade = float(input('Qual sua idade?'))
quer = input('Quer dançar comigo?' )

if altura > 1.60 and peso > 40 and idade >= 18 and quer == 'sim':
    print('Bora simbora!')
else:
    print('Vou ali que meu amigo tá me chamando...')