#Questão 4:

letras = []
vogais = ['a', 'e', 'i', 'o', 'u']

for letra in range(10):
    letra = input('Diga a letra: ')
    letras.append(letra)

qtde = 0
for letra in letras:
    if letra not in vogais:
    #if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'u':
        qtde = qtde + 1
        print(letra)



print(f'foram digitadas {qtde} consoantes.')