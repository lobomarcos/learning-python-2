from random import randint
v = 0
while True:
    jogador = int (input('Digite um valor: '))
    computador = randint (0,10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str (input('Você escolhe Ímpar ou Par? [I/P] ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de: {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print ('Você venceu!')
            v = v + 1 
        else:
            print ('Você perdeu!')
            break

    elif tipo == 'I':
        if total % 2 != 0:
            print ('Você venceu!')
            v = v + 1 
        else:
            print ('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print (f'Cabô! Você venceu {v} vezes.')