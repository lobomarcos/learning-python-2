# NESTE, O USUÁRIO CONSEGUE SELECIONAR O INTERVALO PARA A VERIFICAÇÃO

first = int (input('Digite o número inicial: '))
last = int (input('Digite o número final: '))

soma = 0

for n in range (first, last):
    if n % 3 == 0 and n % 2 != 0:
        soma += n

print (soma)