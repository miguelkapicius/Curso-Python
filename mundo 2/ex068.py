from random import choice
lista=[0,1,2,3,4,5]
par = impar = cont = 0
while True:
    cpu=choice(lista)
    print('[Só valem números de 0 a 5]')
    print(cpu)
    pi=str(input('Par ou ímpar? ')).upper().strip()
    jog=int(input('Seu número: '))
    result= cpu+jog
    if pi=='PAR':
        if result==1:
            print('Derrota')
            break
        elif result==3:
            print('Derrota')
            break
        elif result==5:
            print('Derrota')
            break
        elif result==7:
            print('Derrota')
            break
        elif result==9:
            print('Derrota')
            break
        else:
            print('Venceu essa...')
            cont+=1
    elif pi=='IMPAR':
        if result==2:
            print('Derrota')
            break
        elif result==4:
            print('Derrota')
            break
        elif result==6:
            print('Derrota')
            break
        elif result==8:
            print('Derrota')
            break
        elif result==10:
            print('Derrota')
            break
        else:
            print('Venceu essa...')
            cont+=1
print(f'Você perdeu depois de {cont} vitórias.')
    