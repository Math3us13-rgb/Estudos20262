comprimento = float(input('Informe o comprimento de seu imóvel: '))
largura = float(input('Informe a largura de seu imóvel: '))
imovel = comprimento * largura
vistoria = input('Você possui uma vistoria especial gratuita?')
finalidade = input('Você possui uma finalidade sanitária?')

if imovel > 200 and vistoria == 'sim':
    print('Não pagará nada.')
elif imovel > 200 and vistoria == 'não':
    print('Você deverá pagar 500 reais por metro quadrado.')
    resultado1 = imovel * 500
    print('Você deverá pagar até,', resultado1, 'R$.')
elif imovel <= 200 and finalidade == 'não':
    print('Você deverá pagar até 70 reais por metro quadrado.')
    resultado2 = imovel * 70
    print('você deverá pagar até ', resultado2, 'R$.')
elif imovel <= 200 and finalidade == 'sim':
    print('Você deverá pagar até 120 reais por metro quadrado.')
    resultado3 = imovel * 120
    print('Você deverá pagar até', resultado3,'R$.')
else:
    print('Sem informações o suficiente.')

m2 = float(input('Quantos metros quadrados possui o seu terreno: '))
if m2 > 200:
    resp = input('Você gostaria de requerer uma vistoria gratuita?')
    if resp == 'sim':
        print('Você não precisa pagar nada.')
    else:
        total = 500 * m2
        print('Você pagará', total, 'R$.')
else:
    resp2 = input('Você tem finalidade sanitária?')
    if resp2 == 'sim':
        total = 120 * m2
        print('Você pagará,', total, 'R$ por ter finalidade sanitária.')
    else:
        total = 70 * m2
    print('Você pagará,', total, 'R$.')