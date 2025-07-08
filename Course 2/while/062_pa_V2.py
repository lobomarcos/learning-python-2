firstTerm = int (input('Digite o primeiro termo da p.a.: '))
ratio = int (input('Digite a razão da p.a.: '))
qTerms = int (input('Digite a quantidade de termos da p.a.: '))

term = firstTerm
c = 1 

while c <= qTerms:
    print ('{} -> ' .format(term), end = '')
    term = term + ratio
    c = c + 1 

print ('Fim!')