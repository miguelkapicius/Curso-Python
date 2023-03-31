lista=[]
while True:
    v=(int(input('Adicionar número: ')))
    if v not in lista:
        lista.append(v)
    else:
        print('valor duplicado, não será adicionado...')
    sn=str(input('Deseja continuar? [S/N] ')).upper().strip()
    if sn=='N':
        break
print('-'*70)
lista.sort()
print(f'Foram digitados os valores {lista}')
print('-'*70)
    