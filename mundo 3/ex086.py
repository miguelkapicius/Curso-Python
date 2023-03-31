matriz=[ [0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))

print('-='*8)
print(f'''
{matriz[0]}
{matriz[1]}
{matriz[2]}''')
print('-='*8)
