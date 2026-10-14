#O banco do Brasil abriu uma linha de crédito e está dando empréstimo
#para pessoas que recebem mais de 1800 reais e o valor da parcela do
#empréstimo não pode superar 35% do salário.
#Construa um algoritmo que leia o salário e o valor da parcela,
#informando se o cliente poderá adquirir este empréstimo.

S = float(input('digite seu salário: '))
if S > 1800:

    parcela = float(input('digite a parcela: '))
    porcentagem = (parcela * 100) / S
    if porcentagem <= 35:
        print('empréstimo aprovado')
    else:
        print('este valor da parcela supera 35% do seu salario')

else:
    print('empréstimos neste banco só para quem ganha acima de 1800 reais')