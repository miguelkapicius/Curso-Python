matriz=[ [0,0,0], [0,0,0], [0,0,0]]
par=maior=impar=col=0
for l in range(0,3):
    for c in range(0,3):
       matriz[l][c]= int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):  
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 == 0:
            par+=matriz[l][c]
        elif matriz[l][c] %2==1:
            impar+=matriz[l][c]
    print()
print('-='*30)

print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores ímpares é {impar}')
for l in range(0,3):
    col+=matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {col}')
for c in range(0,3):
    if c ==0:
        maior=matriz[1][c]
    elif matriz[1][c]>maior:
        maior=matriz[1][c]
print(f'O maior valor da 2ª linha é {maior}')
print('-'*60)


