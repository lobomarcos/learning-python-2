# NESTE, O USUÁRIO CONSEGUE SELECIONAR O INTERVALO PARA A VERIFICAÇÃO

first = int (input('Digite o número inicial: '))
last = int (input('Digite o número final: '))

soma = 0
cont = 0

for n in range (first, last):
    if n % 3 == 0 and n % 2 != 0:
        cont = cont + 1
        soma = soma + n

print ('A soma dos {} valores solicitados que ficam entre {} e {} é igual a: {}' .format(cont, first, last, soma))