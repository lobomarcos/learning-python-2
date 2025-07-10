from random import choice

print ('VAMOS JOGAR ÍMPAR OU PAR!')

c = 0
while True:
    userOpt1 = str (input('Escolha entre Ímpar e Par. [I/P]: ')).strip().upper()
    userOpt2 = int (input('Escolha um número de 1 a 10: '))

    pcChoice2 = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = userOpt2 + pcChoice2

    if userOpt1 == 'I' and result % 2 != 0:
        print (f'Você escolheu {userOpt2} e o computador {pcChoice2}. O total é {result}. Você ganhou!')
        c = c + 1
    elif userOpt1 == 'P' and result % 2 == 0:
        print (f'Você escolheu {userOpt2} e o computador {pcChoice2}. O total é {result}. Você ganhou!')
        c = c + 1
    else:
        print (f'Você escolheu {userOpt2} e o computador {pcChoice2}. O total é {result}. Você perdeu!')
        break

print(f'Você ganhou {c} vez(es) consecutivas.')