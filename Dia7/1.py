#Revisão AND:
n = int(input('Digite um número: '))
r = input('O número digitado é par? ').upper()

if n % 2 == 0 and r == 'sim':
    print('Este número é par e você acertou!')

if n % 2 == 1 and r == 'sim':
    print('Este número é impar e você ERROU!')

if n % 2 == 0 and r == 'não':
    print('Este número é par, você ERROU!')

if n % 2 == 1 and r == 'não':
    print('Este número é impar, você acertou!')
else:
    print('Resposta inválida! Digite "sim" ou "não" para obter uma resposta.')