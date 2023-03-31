n=0
sn='S'
soma=0
cont=0
maior=n
menor=n
while sn=='S':
    n=float(input('Digite um número: '))
    sn=str(input('Quer continuar? [S/N] ')).upper().strip()
    soma+=n
    cont+=1
    menor=n
    if n>maior:
        maior=n
    if n<menor:
        menor=n
media=soma/cont
print('Você digitou {} números e a média entre eles foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))