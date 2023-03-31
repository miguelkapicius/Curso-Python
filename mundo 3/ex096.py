def area(l, c):
    mult= l*c
    print(f'A área de um terreno {l}x{c} é de {mult}m².')

print('Controle de Terrenos')
print('-'*22)
l= float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)