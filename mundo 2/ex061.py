print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
termo=int(input('Primeiro termo: '))
razao=int(input('Digite a razão: '))
cont=0
while cont<=10:
    print('{} - '.format(termo), end='')
    termo+=razao
    cont+=1
print('FIM')
