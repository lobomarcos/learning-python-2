num = int(input('Digite um número [999 encerra a contagem]: '))
c = 0
soma = 0

while num != 999:
    soma = soma + num
    c = c + 1
    
    num = int(input('Digite um número [999 encerra a contagem]: '))

print('Contagem encerrada. Você digitou {} números e a soma deles é: {}.'.format(c, soma))