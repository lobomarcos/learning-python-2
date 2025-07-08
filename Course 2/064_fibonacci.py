n = int (input('Quantos termos da Sequência de Fibonnaci você quer mostrar? '))

t1 = 0
t2 = 1
count = 3

print ('Os {} primeiros termos são: ' .format(n))
print ('{} -> {} -> ' .format(t1, t2), end = '')
while count <= n:
    t3 = t1 + t2
    print ('{} -> ' .format(t3), end = '')
    t1 = t2
    t2 = t3
    count = count + 1
print ('Fim!')