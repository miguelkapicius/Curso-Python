import math
catO=float(input('Qual o valor do cateto oposto? '))
catA=float(input('Qual o valor do cateto adjacente? '))
hi= math.hypot(catO,catA)
print('O valor da hipotenusa é {:.2f}'.format(hi))
