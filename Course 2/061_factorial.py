# from math import factorial

n = int(input('Digite um numero para calcular o seu fatorial: '))
c = n
f = 1 

print ('{}! é: ' .format(n), end = '')

while c > 0:
    print ('{}' .format(c), end = ' ')
    print ('x ' if c > 1 else '= ', end = '')
    f = f * c
    c = c - 1

print (f)
# result = factorial(n)

