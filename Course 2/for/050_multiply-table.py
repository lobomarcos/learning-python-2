n = int (input('Digite um número para saber a sua tabuada: '))
print ('A tabuada de {} é: ' .format(n))

for x in range (0, 11):
    multiply = n * x
    print ('{} x {} = {}' .format (n, x, multiply))