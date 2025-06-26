def progressaoAritmetica (firstTerm, ratio, qTerms):

  pa = []
  actualTerm = firstTerm

  for n in range (qTerms):
    pa.append (actualTerm)
    actualTerm = actualTerm + ratio

  return pa

firstTerm = int (input('Digite o primeiro termo da progressão aritmética: '))
ratio = int (input('Digite a razão da progressão aritmética: '))
qTerms = int (input('Digite a quantidade de termos da progressão aritmética: '))

pa = progressaoAritmetica (firstTerm, ratio, qTerms)
print ('A progressão aritmética é:', pa)

for x in range (0, qTerms):
    pa = firstTerm + (qTerms - 1) * ratio
