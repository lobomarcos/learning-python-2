from datetime import date

anoNascimento = int (input('Informe o ano de seu nascimento: '))

hoje = date.today().year
idade = hoje - anoNascimento

if idade <= 9:
    print ('Você tem {} anos de idade e está na Mirim, para atletas de até 9 anos.' .format(idade))
elif 9 < idade <= 14:
    print ('Você tem {} anos de idade e está na categoria Infantil, para atletas até 14 anos.' .format(idade))
elif 14 < idade <= 19:
    print ('Você tem {} anos de idade e está na categoria Junior, para atletas até 19 anos.' .format(idade))
elif idade == 20:
    print ('Aos 20 anos de idade você se encaixa na categoria Senior.')
elif idade > 20:
    print ('Você tem {} anos de idade e se enquadra na categoria Master.' .format(idade))