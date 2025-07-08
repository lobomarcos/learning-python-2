pesoMaior = 0
pesoMenor = 0

for p in range (1, 6):
    peso = float (input('Qual o peso da {}º pessoa?: ' .format(p)))

    if p == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

print('O menor peso foi: {} KG.'.format(pesoMenor))
print('O maior peso foi: {} KG.'.format(pesoMaior))