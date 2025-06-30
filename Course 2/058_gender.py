g = input('Com qual gênero você se identifica? [M / F] ').upper()

while g != 'M' and g != 'F':
    print('Essa opção não existe, tente novamente.')
    g = input('Com qual gênero você se identifica? [M / F] ').upper()

print('Você digitou:', g)