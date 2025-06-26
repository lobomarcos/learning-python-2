firstTerm = int (input('Digite o primeiro termo da progressão aritmética: '))
ratio = int (input('Digite a razão da progressão aritmética: '))
q = int (input('Digite a quantidade de termos da progressão aritmética: '))

qTerms = firstTerm + (q - 1) * ratio

for x in range (firstTerm, qTerms + ratio, ratio):
    print (x, end = ' -> ')