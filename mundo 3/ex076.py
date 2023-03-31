lista =('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)
print('-'*30)
for i in range (0, len(lista)):
    if i %2 ==0:
        print(f'{lista[i]:.<25}', end='')
    elif i%2 == 1:
        print(f'{lista[i]}')
