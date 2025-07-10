number = int (input('Digite um número para saber a sua tabuada: '))

if number > 0:
    print ('A tabuada de {} é: ' .format(number))

for x in range (0, 11):
    if number < 0:
        print ('Número negativo não possui tabuada.')
        break
    
    multiply = number * x
    print ('{} x {} = {}' .format (number, x, multiply))