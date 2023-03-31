nome=preco=prox=nomebarato=barato=soma=mais1000=0
cont=0
print('='*40)
print('{:^40}'.format('MERCADINHO BIG BOM'))
print('='*40)
while True:
    nome=str(input('Nome do produto: ')).strip()
    preco=float(input(f'Preço de {nome}: R$'))
    prox=str(input('Quer continuar? [S/N] ')).upper().strip()
    cont+=1
    soma+=preco
    if preco>1000:
        mais1000+=1
    if cont==1:
        barato=preco
        nomebarato=nome
    if preco<barato:
        barato=preco
        nomebarato=nome
    if prox=='N':
        print('Pedido finalizado!')
        break
print(f'TOTAL DA COMPRA: R${soma}')
print(f'{mais1000} custam mais de R$1000')
print(f'O produto mais barato é {nomebarato} custando um total de R${barato}')