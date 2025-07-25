total = totalmil = 0

while True:
    produtoNome = str (input('Qual é o nome do produto? '))
    produtoPreco = float (input('Qual é o seu preço? R$ '))
    total = total + produtoPreco

    if produtoPreco > 1000:
        totalmil = totalmil + 1

    resp = ' '
    while resp not in 'SN':
        opt = str (input('Você quer registrar mais produtos? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print (f'O total da compra é {total:10.2f}.')
print (f'Há {totalmil} produtos custando mais que R$ 1000,00.')