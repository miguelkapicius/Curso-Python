r1=float(input('Valor do primeiro segmento: '))
r2=float(input('Valor do segundo segmento: '))
r3=float(input('Valor do terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    if r1==r2==r3:
        print('EQUILÁTERO')
    elif r1!=r2!=r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não forma um triângulo')


