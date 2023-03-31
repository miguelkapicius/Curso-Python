def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont=i
        while cont<=f:
            print(f'{cont} ', end='')
            cont+=p
        print('FIM')
    else:
        cont=i
        while cont>=f:
            print(f'{cont} ', end='')
            cont-=p
        print('FIM')

print('-='*30)
contador(1, 10, 1)
print('-='*30)
contador(10, 0, 1)
print('-='*30)
print('SUA VEZ!!! Personalize o contador:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)