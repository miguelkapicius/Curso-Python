def maior(*num):
    cont=0
    maior=0
    print('-='*30)
    print('Os valores passados foram...')
    for v in num:
        print(f'{v} ', end='',)
        if cont == 0:
            maior = v
        if v > maior:
            maior = v
        cont+=1
    print(f'\nForam passados {cont} valores')
    print(f'o maior número é: {maior} ')
    print('-='*30)


maior(2,99,1000,43,2,5,7,5,3,2,1)