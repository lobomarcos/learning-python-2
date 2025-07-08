n = int (input('Quantos números da Sequência de Fibonnaci você quer mostrar? '))

t1 = 0
t2 = 1
count = 3

print ('Os {} primeiros números da Sequência de Fibonacci é: ' .format(n))
print ('{} -> {} -> ' .format(t1, t2), end = '')
while count <= n:
    t3 = t1 + t2
    print ('{} -> ' .format(t3), end = '')
    t1 = t2
    t2 = t3
    count = count + 1
print ('Fim!')