nascimento=int(input('Qual o ano de nascimento? '))
idade= 2022-nascimento
if idade<18:
    print('Você ainda vai se alistar!')
    falta=18-idade
    print('Faltam {} anos para o alistamento!'.format(falta))
elif idade>18:
    print('Já passou o tempo de alistamento!')
    falta=idade-18
    print('O tempo excedeu por {} anos'.format(falta))
else:
    
    print('Você precisa se alistar agora!')
