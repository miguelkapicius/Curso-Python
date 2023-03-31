pess=[]
final=[]
maior=menor=0
while True:
    pess.append(str(input('Digite o nome: ')))
    pess.append(float(input('Digite o peso: ')))
    if len(final)==0:
        menor=maior=pess[1]
    elif pess[1]> maior:
        maior=pess[1]
    elif pess[1]<menor:
        menor=pess[1]
    final.append(pess[:])
    pess.clear()
    r=str(input('Quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
print('-='*45)
print(f'Foram cadastradas {len(final)} pessoas')
print(f'O maior peso foi de {maior}Kg, ', end='')
for p in final:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg, ', end='')
for p in final:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print('-='*45)
