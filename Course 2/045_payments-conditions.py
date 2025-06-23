value = float (input('Qual o valor do produto que você deseja comprar?: ')) 
payment = int (input('Qual seria a forma de pagamento?. \nFormas de pagamento: \n [ 1 ] À vista em dinheiro \n [ 2 ] À vista no Cartão de Crédito \n [ 3 ] 2x no Cartão de Crédito \n [ 4 ] 3x no Cartão de Crédito \n'))

discountMoney = value * 0.1
onMoney = value - discountMoney

discountCard = value * 0.05
onCard = value - discountCard

onCard2 = value 

taxCard = value * 0.2
onCard3 = value + taxCard

if payment == 1: 
    print ('Pagando o produto à vista em dinheiro, você ganha 10% de desconto. O novo valor é: R$', onMoney)
elif payment == 2:
    print ('Pagando o produto à vista no cartão, você ganha 5% de desconto. O novo valor é: R$', onCard)
elif payment == 3:
    print ('Pagando o produto em até 2x no cartão, não há desconto. O valor é: R$', onCard2)
elif payment == 4:
    print ('Pagando o produto em até 3x no cartão, há juros de 20%. O novo valor é: R$', onCard3)