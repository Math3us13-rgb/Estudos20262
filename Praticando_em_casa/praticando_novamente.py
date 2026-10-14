print('Tudo bem, em mais uma aula prática.' 
      '\nQuero que siga as demais instruções, entendido?')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
s = n1 + n2
print('Ok ok, temos um resultado!' 
      '\nSua soma deu um total de {}'.format(s))
print('Agora para termos ciência do tipo do valor de soma é bem simples!'
      '\n basta fazer o seguinte:')
print(type(s))

print('Há! Não está satisfeito, tudo bem, então que tal assim:'
      '\nA soma entre {} e {} é igual a {}'.format(n1, n2, s))

print('Ainda não se deu por vencido? Ok ok...')
print('Verifique se o valor de sua soma foi verdadeiro ou falso então:')
vf = bool(input('Digite exatamente o valor de sua soma acima: '))
print(vf)
