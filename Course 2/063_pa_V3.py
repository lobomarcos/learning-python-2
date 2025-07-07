firstTerm = int (input('Digite o primeiro termo da p.a.: '))
ratio = int (input('Digite a razão da p.a.: '))
qTerms = int (input('Digite a quantidade de termos da p.a.: '))

term = firstTerm
c = 1 

t = 0
opt = qTerms

while opt != 0:
    t = t + opt
    while c <= t:
        print ('{} -> ' .format(term), end = '')
        term = term + ratio
        c = c + 1
    print ('Pausa!')

    opt = int(input('\nQuantos termos você quer mostrar a mais? '))

    if opt == 0:
        print ('Fim!')