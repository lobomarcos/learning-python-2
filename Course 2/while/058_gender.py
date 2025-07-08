g = input('Com qual sexo você se identifica? [M / F] ').strip().upper()[0]

while g != 'M' and g != 'F':
    print('Essa opção não existe, tente novamente.')
    g = input('Com qual sexo você se identifica? [M / F] ').strip().upper()[0]

print('Você digitou:', g)