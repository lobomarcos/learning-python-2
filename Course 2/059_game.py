import random
from time import sleep

print ('Pensei em um número!')

numberUser = int (input('Digite um número entre 0 e 10: '))
print ('Processando...')
sleep(1)

numberRandom = random.randint(0, 10)
tCount = 1

while numberUser != numberRandom:
    print ('Você não consegue ler meus pensamentos!')
    numberUser = int (input('Digite um número entre 0 e 10: '))
    print ('Processando...')
    sleep(1)

    tCount = tCount + 1

if numberUser == numberRandom:
    print ('Você conseguiu advinhar o número que eu pensei!')


print ('Eu pensei no número {}!' .format (numberRandom))
print ('Você tentou advinhar {} vezes até vencer!' .format (tCount))