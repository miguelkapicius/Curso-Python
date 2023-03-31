nasc=int(input('Ano de nascimento: '))
anos= 2022-nasc
if anos<=9:
    print('MIRIM')
elif anos<=14:
    print('INFANTIL')
elif anos<=19:
    print('JUNIOR')
elif anos<=20:
    print('SÊNIOR')
else:
    print('MASTER')
