express=str(input('Digite uma expressão: '))
lista=[]
for letra in express:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é inválida!')