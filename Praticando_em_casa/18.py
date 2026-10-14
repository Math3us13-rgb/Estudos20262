#Estrutura de decisão - Questão 18:
from email import message_from_binary_file
from tkinter.filedialog import dialogstates

data = int(input('Por favor informe a data de seu nascimento no formato dd/mm/aaa:'))
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

if data >= 00/00/0000:
    print('Data valida.')
else:
    print('Data invalida.')