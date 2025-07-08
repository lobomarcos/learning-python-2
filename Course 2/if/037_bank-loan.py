name = str (input('Qual é o seu nome?: '))
value = float (input('Qual o valor do empréstimo?: '))
wage = float (input('Qual o seu salário?: '))
payOff = float (input('Em até quantos anos você deseja quitar o empréstimo?: '))

portion = (value / 12) / payOff

if portion > wage * 0.3:
    print ('Sr(a). {}, infelizmente, seu impréstimo foi negado. A parcela mensal ficaria acima de 30% do seu salário.' .format(name))
else:
    print ('Parabéns, Sr(a). {}! Seu empréstimo foi aprovado.' .format(name))

print ('Cliente: {}.' .format(name))
print ('Parcela mensal: {:.2f}.' .format(portion))