from time import sleep

# TIMER - CONTAGEM REGRESSIVA - SELECIONÁVEL

start = int (input('Digite o tempo desejado para a contagem regressiva: '))
for t in range(start, -1, -1):
    print (t)
    sleep (1)

print ('Fogos!')