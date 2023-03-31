n=0
while True:
    n=int(input('Digite um número para fazer a tabuada: '))
    if n<0:
        break
    print('-'*30)
    for t in range (1,11):
        print(f'{n}x{t}={n*t}')
    print('-'*30)
print('Encerrado, volte sempre!!!')
