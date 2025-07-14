produtos = 0
c1 = 0

while True:
    produtoNome = str (input('Qual é o nome do produto? '))
    produtoPreco = float (input('Qual é o seu preço? R$ '))
    opt = str (input('Você quer registrar mais produtos? [S/N] '))

    if produtoPreco < 1000:
        c1 = c1 + 1
        print(f'Há {c1} produtos com preço maior que R$ 1000,00.')

    if opt == 'N':
        break