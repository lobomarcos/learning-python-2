print ('CADASTRO DE PESSOAS')

sM = sF = 0
i = iM = iF = 0

while True:
    sexo = str (input('Você se identifica com qual gênero? [M/F] ')).strip().upper()[0]
    idade = int (input('Quantos anos você tem? '))
    opt = str (input('Você deseja cadastrar mais pessoas no sistema? [S/N] ')).strip().upper()[0]

    if sexo == 'M':
        sM = sM + 1
        print(f'Há {sM} pessoas identificadas com o sexo masculino cadastradas no sistema.')
    elif sexo == 'F':
        sF = sF + 1 
        print(f'Há {sF} pessoas identificadas com o sexo feminino cadastradas no sistema.')

    if idade > 18:
        i = i + 1
        print(f'Há {i} pessoas com mais de 18 anos de idade cadastradas no sistema.')
    elif idade < 20 and sexo == 'F':
        iF = iF + 1
        print(f'Há {iF} mulheres com menos de 20 anos de idade cadastradas no sistema.')

    if opt == 'N':
        break
    