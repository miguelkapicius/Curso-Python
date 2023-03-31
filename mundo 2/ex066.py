n = soma = cont = 0
while True:
    n=int(input('Digite um número: '))
    cont+=1
    if n==999:
        break
    soma+=n
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
