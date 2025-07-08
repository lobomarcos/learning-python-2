from time import sleep

# TIMER - CONTAGEM PROGRESSIVA OU REGRESSIVA - SELECIONÁVEL
option = int (input('''Você quer fazer uma contagem Progressiva ou Regressiva?
[ 1 ] Progressiva
[ 2 ] Regressiva
'''))

if option == 1:
    start = int (input('Digite o tempo desejado para a contagem progressiva: '))
    for t in range (1, start + 1):
        print (t)
        sleep (1)
    print ('Fogos!')

elif option == 2:
    startR = int (input('Digite o tempo desejado para a contagem regressiva: '))
    for t in range (startR, -1, -1):
        print (t)
        sleep (1)
    print ('Fogos!')