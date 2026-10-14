soma = 0
i = 0
while i < 5:
    idade = int(input("Digite sua idade: "))
    soma = soma + idade
    i = i + 1

print('A soma de idade foi', soma)
media = soma / 5
print('A média de idade na sala é de:', media)