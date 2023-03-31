km=int(input('Quantos km? '))
if km > 200:
    preco= km* 0.45
    print('Sua viagem custa {}'.format(preco))
else:
    preco= km* 0.50
    print('Sua viagem custa {}'.format(preco))