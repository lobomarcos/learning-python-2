from datetime import date

atual = date.today().year

totMaior = 0
totMenor = 0

for a in range (1, 8):
    nasc = int (input('Digite o ano de nascimento da {}º pessoa: ' .format(a)))

    age = atual - nasc

    if age > 18:
       # print ('Essa pessoa nasceu em {} e tem {} anos. Portanto é maior de idade.' .format(nasc, age))
        totMaior += 1
    else:
       # print ('Essa pessoa nasceu em {} e tem {} anos. Portanto NÃO é maior de idade.' .format(nasc, age))
        totMenor += 1
    
print ('Ao todo, temos {} pessoas maiores de idade.' .format(totMaior))
print ('E também temos {} pessoas menores de idade.' .format(totMenor))
