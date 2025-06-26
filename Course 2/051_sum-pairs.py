sumPairs = 0
count = 0

for x in range (1, 7):
    num = int (input('Digite o {}º número inteiro: ' .format(x)))
    if num % 2 == 0:
        sumPairs = sumPairs + num
        count = count + 1

print ('A soma dos números {} pares informados é: {}' .format(count, sumPairs))