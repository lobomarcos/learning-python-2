from time import sleep

opt = ''

while opt != 5:

    print ('Carregando menu...')
    sleep(1)

    opt = int (input('''Escolha uma opção para efetuar uma operação matemática:
    [ 1 ] SOMA
    [ 2 ] SUBTRAÇÃO
    [ 3 ] MULTIPLICAÇÃO
    [ 4 ] DIVISÃO
    [ 5 ] SAIR
    '''))
    
    print ('Carregando a opção número {}...' .format(opt))
    sleep(1)

    if opt == 1:
        print ('Você escolheu SOMAR!')
    
        sum1 = int (input('Digite um número: '))
        sum2 = int (input('Digite mais um número: '))

        s = sum1 + sum2

        print ('A soma entre {} e {} é: {}.' .format(sum1, sum2, s))

    elif opt == 2:
        print ('Você escolheu SUBTRAIR!')

        sub1 = int (input('Digite um número: '))
        sub2 = int (input('Digite outro número: '))

        subt = sub1 - sub2

        print ('A subtração entre {} e {} é: {}.' .format(sub1, sub2, subt))

    elif opt == 3: 
        print ('Você escolheu MULTIPLICAR!')

        m1 = int (input('Digite um número: '))
        m2 = int (input('Digite outro número: '))

        mult = m1 * m2

        print ('A multiplicação entre {} e {} é: {}.' .format(m1, m2, mult))

    elif opt == 4:
        print ('Você escolheu DIVIDIR!')

        d1 = int (input('Digite um valor: '))
        d2 = int (input('Digite outro valor: '))

        div = d1 / d2

        print ('A divisão entre {} e {} é: {}.' .format(d1, d2, div))

    elif opt == 5:
        print ('Saindo...')
        sleep(1)
        print('Programa encerrado!')

    else:
        print ('Opção inexistente. Tente novamente.')