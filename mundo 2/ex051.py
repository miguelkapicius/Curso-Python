print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
termo=int(input('Primeiro termo: '))
razao=int(input('Razão: '))
decimo= termo + (10-1)* razao
for c in range(termo,decimo+razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
