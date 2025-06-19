sideA = float (input('Digite o tamanho do Lado A: '))
sideB = float (input('Digite o tamanho do Lado B: '))
sideC = float (input('Digite o tamanho do Lado C: '))

allSides1 = sideA + sideB
allSides2 = sideA + sideC
allSides3 = sideB + sideC

if sideA + sideB == allSides1 > sideC:
    print('Com {} + {} = {} > {}, é possível formar um triângulo.' .format (sideA, sideB, allSides1, sideC))
else:
    print('Não é possível formar um triângulo com esses valores.')

if sideA + sideC == allSides2 > sideB:
    print('Com {} + {} = {} > {}, é possível formar um triângulo.' .format (sideA, sideC, allSides2, sideB))
else:
    print('Não é possível formar um triângulo com esses valores.')

if sideB + sideC == allSides3 > sideA:
    print('Com {} + {} = {} > {}, é possível formar um triângulo.' .format (sideB, sideC, allSides3, sideA))
else:
    print('Não é possível formar um triângulo com esses valores.')

if sideA == sideB == sideC:
    print ('Este é um triângulo equilátero, pois todos os seus lados são iguais.')
elif sideA == sideB != sideC or sideB == sideA != sideC or sideC == sideB != sideA:
    print ('Este é um triângulo isósceles, pois apenas 2 dos seus lados são iguais.')
elif sideA != sideB != sideC:
    print ('Este é um triângulo escaleno, pois nenhum dos seus lados tem a mesma medida.')