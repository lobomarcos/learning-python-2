import random

print ('Vamos jogar Jokenpô!')
userOpt = int (input('Escolha entre Pedra, Papel e Tesoura! \n 1. Pedra \n 2. Papel \n 3. Tesoura \n'))

jokenpoList = ['Pedra', 'Papel', 'Tesoura']
jokenpoChoice = random.choice (jokenpoList)

# QUANDO O USUÁRIO GANHA
if userOpt == 1 and jokenpoChoice == 'Tesoura':
    print ('Você ganhou! Pedra ganha de Tesoura!')

elif userOpt == 2 and jokenpoChoice == 'Pedra':
    print ('Você ganhou! Papel ganha de Pedra!')

elif userOpt == 3 and jokenpoChoice == 'Papel':
    print ('Você ganhou! Tesoura ganha de papel!')

# QUANDO O USUÁRIO PERDE
elif userOpt == 1 and jokenpoChoice == 'Papel':
    print ('Você perdeu! Papel ganha de Pedra!')

elif userOpt == 2 and jokenpoChoice == 'Tesoura':
    print ('Você perdeu! Tesoura ganha de Papel!')

elif userOpt == 3 and jokenpoChoice == 'Pedra':
    print ('Você perdeu! Pedra ganha de Tesoura!')

# QUANDO HÁ EMPATE
elif userOpt == 1 and jokenpoChoice == 'Pedra':
    print ('Empate! Vamos de novo!')

elif userOpt == 2 and jokenpoChoice == 'Papel':
    print ('Empate! Vamos de novo!')

elif userOpt == 3 and jokenpoChoice == 'Tesoura':
    print ('Empate! Vamos de novo!')