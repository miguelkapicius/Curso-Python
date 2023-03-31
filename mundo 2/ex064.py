n=0
cont=0
soma=0
while n!=999:
    n=int(input('Digite um número [999 para parar]: '))
    cont+=1
    if n!=999:
        soma+=n
print('Você digitou {} numeros e a soma deeles foi {}.'.format(cont, soma))

