lista=[]
cont=0
while True:
    lista.append(int(input('Digite um valor: ')))
    r=str(input('Quer continuar? [S/N] ')).upper().strip()
    cont+=1
    if r=='N':
        break
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os elementos em ordem decrescente são {lista} ')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontrado!')