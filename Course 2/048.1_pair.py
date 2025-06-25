# VERIFICANDO NÚMEROS PARES EM UM INTERVALO DETERMINADO PELO USUÁRIO.

insert = int (input('Qual o número inicial?: '))
insert2 = int (input('Qual o número final?: '))

count = 0

for n in range (insert, insert2 + 1):
    if n % 2 == 0:
        print ('é par!')
        count += 1
    print (n)

print('Quantidade de números pares:', count)