luz = int(input('Digite o valor do sensor de luminosidade: '))
temp = int(input('Digite o valor do sensor de temperatura: '))
umid = int(input('Digite o valor do sensor de umidade: '))
pres_intra = input('Tem presença interna?')
pres_exter = input('Tem presença externa na janela? ')
hr = int(input('Digite o valor das horas: '))

if luz >= 7 and hr >= 5 and pres_intra == 'sim':
    print('Feche a janela.')
    print('Ligando o ar-condicionado...')
elif umid < 45 and temp < 22 and pres_intra == 'sim' and (hr > 23 or hr < 7) and pres_exter == 'sim':
    print('')
    print('')