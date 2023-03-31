import math
ang=float(input('Qual o valor do ângulo? '))
seno= math.sin(math.radians(ang))
cose= math.cos(math.radians(ang))
tang= math.tan(math.radians(ang))
print('O seno de {} tem o valor de {:.2f}'.format(ang,seno))
print('Cosseno de {:.2f}'.format(cose))
print('E tangente de{:.2f}'.format(tang))
