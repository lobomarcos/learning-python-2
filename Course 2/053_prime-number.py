pNumber = int(input('Digite um número para saber se ele é Primo: '))
div = 0 

for x in range (1, pNumber + 1):
    print(x, end = ' ')
    if pNumber % x == 0:
        print('[ OK ]')
        div = div + 1
    else:
        print('[ X ]')

print ('\033[0;34mO número {} foi divisível {} vezes.' .format(pNumber, div))

if div == 2:
    print ('\033[0;32mPor isso, é um número primo.')
else:
    print ('\033[0;31mPortanto, NÃO é um número primo.')