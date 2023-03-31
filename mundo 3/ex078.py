valor=[]
maior = 0
menor = 0
for v in range(0,5):
    valor.append(int(input('Insira um valor na lista: ')))
    if v==0:
        maior=valor[v]
        menor=valor[v]
    else:
        if valor[v]> maior:
            maior=valor[v]
        if valor[v]<menor:
            menor=valor[v]
print(f'A lista é {valor}')
print(f'O maior valor da lista é {maior} na(s) posição(s): ', end='')
for i, v in enumerate(valor):
    if v==maior:
        print(f'{i}...', end='')
print(f'\nO menor valor da lista é {menor} na(s) posição(s): ', end='')
for i, v in enumerate(valor):
    if v==menor:
        print(f'{i}...', end='')

