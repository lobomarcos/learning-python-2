number = int (input('Digite um número para saber a sua tabuada: '))

if number > 0:
    print ('A tabuada de {} é: ' .format(number))

while number > 0:
    if number < 0:
        print ('Número negativo não possui tabuada.')
        break
        
    for x in range (0, 11):

        multiply = number * x
        print ('{} x {} = {}' .format (number, x, multiply))

    number = int (input('De qual outro número você gostaria de ver a tabuada? '))