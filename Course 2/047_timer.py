from time import sleep

# TIMER DE 10 A 0 - CONTAGEM REGRESSIVA
'''
for t in range (10, -1, -1):
    print (t)
    sleep(1)

print ('Fogos!')
'''

# TIMER - CONTAGEM REGRESSIVA - SELECIONÁVEL

start = int (input('Digite o tempo desejado para a contagem regressiva: '))
for t in range(start, -1, -1):
    print (t)
    sleep (1)

print ('Fogos!')