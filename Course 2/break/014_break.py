# BREAK - INTERROMPE ESTRUTURAS DE REPETIÇÕES

# EX 1.:
n = s = 0
while True:
    n = int (input('Digite um número: '))
    # Exclui a necessidade de declarar um valor de parada no WHILE (e de gambiarras)
    if n == 999:
        break
    s = s + n

print('A soma dos números vale: {}.' .format(s))