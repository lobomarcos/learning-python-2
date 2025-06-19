nota1 = float (input('Digite a 1ª nota: '))
nota2 = float (input('Digite a 2ª nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print ('Sua média foi: {}. Infelizmente, você foi reprovado(a).' .format(media))
elif 5.0 <= media < 6.9:
    print ('Sua média foi: {}. Você está de recuperação.' .format(media))
elif media >= 7.0:
    print ('Sua média foi: {}. Parabéns, você foi aprovado(a)!' .format(media))
    