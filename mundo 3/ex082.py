lista=[]
pares=[]
impares=[]
while True:
    n=(int(input('Digite um valor: ')))
    lista.append(n)
    r=str(input('quer continuar? [S/N] '))
    if n % 2 == 0:
        pares.append(n)
    elif n %2 == 1:
        impares.append(n)
    if r in 'Nn':
        break
lista.sort()
print('-='*40)
print(lista)
print(f'{pares} São os pares')
print(f'{impares} São os ímpares')
print('-='*40)
