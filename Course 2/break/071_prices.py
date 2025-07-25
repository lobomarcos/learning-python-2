total = totalmil = menor = cont = 0

while True:
    produtoNome = str (input('Qual é o nome do produto? '))
    produtoPreco = float (input('Qual é o seu preço? R$ '))
    cont = cont + 1
    total = total + produtoPreco

    if produtoPreco > 1000:
        totalmil = totalmil + 1

    if cont == 1 or produtoPreco < menor: 
        menor = produtoPreco
    else: 
        if produtoPreco < menor:
            menor = produtoPreco

    opt = ' '
    while opt not in 'SN':
        opt = str (input('Você quer registrar mais produtos? [S/N] ')).strip().upper()[0]
    if opt == 'N':
        break

print (f'O total da compra é R$ {total:10.2f}.')
print (f'Há {totalmil} produtos custando mais que R$ 1000,00.')
print (f'O produto mais barato custa R$ {menor:.2f}.')