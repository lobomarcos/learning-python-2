from datetime import date

anoNascimento = int (input('Informe o ano de seu nascimento: '))

hoje = date.today().year
idade = hoje - anoNascimento
idadeAlistamento = 18

if idade < idadeAlistamento:
    print ('Você tem {} anos. Faltam {} anos para o momento de você se alistar para o exército.' .format (idade, idadeAlistamento - idade))
elif idade == idadeAlistamento:
    print ('Você tem {} anos. Já está na hora do seu alistamento militar.' .format (idadeAlistamento))
else:
    print ('Você tem {} anos. Já se passaram {} anos do mommento de se alistar para o exército.' .format(idade, idade - idadeAlistamento))
        