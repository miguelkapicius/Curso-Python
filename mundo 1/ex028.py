import random
lista=[0,1,2,3,4,5]
n = random.choice(lista)
n2=(int(input(' tente adivinhar o número de 0 a 5: ')))
if n2 == n:
    print('Parabéns, você acertou!!!')
else:
    print('Não foi dessa vez :(')
