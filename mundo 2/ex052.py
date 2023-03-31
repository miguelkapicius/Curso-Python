n=int(input('Digite um número inteiro: '))
tot=0
for c in range(1,n+1):
    if n % c ==0:
        print('\033[34m', end='')
        tot+=1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('''\033[m
O número {} foi divisível {} vezes'''.format(n, tot))
if tot==2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')
