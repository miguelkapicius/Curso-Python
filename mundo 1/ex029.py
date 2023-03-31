vel=int(input('A qual velocidade está o carro: '))
if vel > 80:
    multa= (vel-80)*7
    print('Sua multa por estar acima da velocidade é: {}'.format(multa))
else:
    print('Tudo certo!')    
