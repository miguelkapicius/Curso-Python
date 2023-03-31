from random import randint
numeros=[]

def sorteia(lista):
    for v in range(0,5):
        n=randint(0,10)
        lista.append(n)
    print(lista)


def somaPar(lista):
    soma=0
    for o in lista:
        if o %2 == 0:
            soma += o
    print(f'A soma dos números pares foi {soma}')


print('-='*30)
sorteia(numeros)
somaPar(numeros)


