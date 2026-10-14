#Estrutura de decisão - Questão 12:

hora = float(input('Digite quanto ganha por hora: '))
horas_trab = int(input('Digite quantas horas trabalha: '))
sal_bruto = hora * horas_trab

if sal_bruto < 901:
    print('Insento de imposto.')
elif sal_bruto <= 1500:
    desconto_ir = sal_bruto * 0.05
    print('com 5% de desconto, seu salário será de', desconto_ir, 'R$.')
elif sal_bruto <= 2500:
    desconto_inss = sal_bruto * 0.10
    print('com 10% de desconto, seu salário será de', desconto_inss, 'R$.')
elif sal_bruto > 2500:
    desconto_fgts = sal_bruto * 0.20
    print('Seu salário de', sal_bruto, 'R$ graças aos descontos, passará a ser de', desconto_fgts, 'R$.')
