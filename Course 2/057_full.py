somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher = 0

for i in range (1, 5):

    print ('----' ' PESSOA {} ' '-----' .format(i))

    name = str (input('Qual o nome da Pessoa {}? ' .format(i))) .strip()

    age = int (input('Qual a idade da Pessoa {}? ' .format(i)))
    somaIdade = somaIdade + age

    gender = str (input('Qual o sexo da Pessoa {}? [M / F]' .format(i))) .strip()

    if i == 1 and gender == 'Mm':
        maiorIdadeHomem = age
        nomeVelho = name

    if gender in 'Mm' and age > maiorIdadeHomem:
        maiorIdadeHomem = age
        nomeVelho = name

    if gender in 'Ff' and age < 20:
        totMulher = totMulher + 1

mediaIdade = somaIdade / 4

print ('A média de idade das 4 pessoas é: {}.' .format(mediaIdade))
print ('O homem mais velho do grupo tem {} anos e se chama {}.' .format(maiorIdadeHomem, nomeVelho))
print ('{} mulher(es) tem menos que 20 anos.' .format(totMulher))