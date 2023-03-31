import math
n=int(input('Digite um número para fatorar: '))
cont=n
f= math.factorial(n)
while cont>=1:
    print('{}'.format(cont), end='')
    print('x'if cont>1 else '=', end='')
    cont-=1
print(' >>>> O fatorial de {} é {}'.format(n,f))
