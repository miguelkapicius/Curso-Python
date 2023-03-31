ano=int(input('Qual ano estamos? '))
res= ano%4
if res==0:
    print('é um ano bissexto')
else:
    print('Não é um ano bissexto')
