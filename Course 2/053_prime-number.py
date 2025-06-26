pNumber = int(input('Digite um número para saber se ele é Primo: '))

if pNumber < 2:
    print('{} não é um número primo.'.format(pNumber))
else:
    isPrime = True
    for i in range(2, int(pNumber ** 0.5) + 1):
        if pNumber % i == 0:
            isPrime = False
            break
    if isPrime:
        print('{} é um número primo.'.format(pNumber))
    else:
        print('{} não é um número primo.'.format(pNumber))