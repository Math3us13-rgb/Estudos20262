#print
a = 2
b = 3
#f string -> format
print(f'meu número preferido é o {a} mas eu gosto do {b}')

#format
print('eu estou cansado de {} e {}'.format(a,b))

#type
#mostra o tipo de uma variável.

nome = 'Rene'
idade = 31
altura = 1.75

print(type(nome))
print(type(idade))
print(type(altura))

#for -> Estrutura e repetição
#Usada em situações onde a quantidade de repetições é definida.

for letra in 'cadeira':
    print(letra)

#range
#1- Parâmetro: serve para indicar onde inicia a contagem.
#2- parâmetro: serve para contar a condição de parada.
#OBS: se colocar apenas um parâmetro, ele inicia de 0.