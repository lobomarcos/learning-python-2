r = 'S'
soma = quant = media = maior = menor = 0

# OK
while r in 'Ss':
    num = int (input('Digite um número: '))

    soma = soma + num
    quant = quant + 1

    if quant == 1: 
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    r = str (input('Quer continuar digitando números? [S/N]: ')).strip().upper()

# OK
if r in 'N':
    media = soma / quant
    print('Você digitou {} números e a média é: {}.' .format(quant, media))
    print('O maior número digitado foi {} e o menor número digitado foi {}.' .format(maior, menor))