#Um casal de alunos está precisando de um sistema para ler a nota e a
#frequência do casal nas aulas. O sistema deve aprovar o aluno mesmo que
#ele tenha obtido nota inferior a 7, porém a frequência precisa ser 100%
#e a nota não pode ser menor que 6.
#O algoritmo deve receber 2 dados: Nota e Frequência.
#OBS: Menos de 75% de frequência reprova.

n = float(input ('Digite a nota: '))
f = int(input ('Digite a frequência em porcentagem: '))

if (n >= 7 and f == 75) or (n >= 6 and f == 100):
    print('Aprovado(a)')
else:
    print('Reprovado(a)')