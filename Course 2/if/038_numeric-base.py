number = int (input('Digite um número inteiro: '))

bi = bin(number)
oct = oct(number)
hex = hex(number)

print ('O número {} em binário é: {}.' .format(number, bi[2:]))
print ('O número {} em octal é: {}.' .format(number, oct[2:]))
print ('O número {} em hexadecimal é: {}.' .format(number, hex[2:]))