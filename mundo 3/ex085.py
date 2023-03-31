lista= [[], []]
for c in range(1,8):
    n=int(input(f'Digite o {c}º valor: '))
    if n %2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os números pares são: {lista[0]}')
print(f'Os números ímpares são: {lista[1]}')
print('-='*30)
