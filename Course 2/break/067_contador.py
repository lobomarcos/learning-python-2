contador = 0
numero = 0

while True:
    numero = int (input('Digite um número: '))
    print ('Para encerrar, digite 999.')

    if numero == 999:
        break

    contador = contador + numero

print ('A soma dos números digitados é: {}.' .format(contador))