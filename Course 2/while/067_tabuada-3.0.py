while True:
    n = int (input('Digite um número para saber a sua tabuada: '))
    if n > 0:
        print ('A tabuada de {} é: ' .format(n))

    elif n < 0:
        print ('Não é possível gerar tabuada de número negativo.')
        break

    for x in range (0, 11):
        multiply = n * x
        print ('{} x {} = {}' .format (n, x, multiply))