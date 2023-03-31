soma=0
cont=0
for n in range(1,7):
    n=(int(input('Digite o valor: ')))
    if n %2==0:
        soma+=n
        cont+=1
print('Você informou {} números pares e a soma deles é {} '.format(cont, soma))
