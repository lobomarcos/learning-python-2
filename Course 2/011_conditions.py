# CONDIÇÕES ANINHADAS
# else - elif (dá pra usar or, in, and junto do elif) - else

# if - else
nome = str (input('Qual é o seu nome? '))

if nome == 'Marcos':
    print ('Seu nome é muito legal!')
elif nome == 'Pedro' or nome == 'Lucas' or nome == 'Maria':
    print ('Seu nome é bem popular!')
elif nome in 'Ana Karina Giulia':
    print ('Com certeza é um nome feminino!')
else: 
    print ('Seu nome é beeeem comum...')

print ('Prazer em te conhecer, {}!' .format(nome))

# PAREI EM 16 MINUTOS!!!