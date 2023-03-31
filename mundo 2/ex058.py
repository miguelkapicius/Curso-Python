import random
print('''Sou seu computador...
Acabei de pensar em um número de 1 a 10
Será que você consegue adivinhar?''')
lista=[1,2,3,4,5,6,7,8,9,10]
cpu= random.choice(lista)
n=int(input('Me diga seu chute: '))
cont=0
while n>cpu:
    n=int(input('É MENOS que isso, diga outro chute: '))
    cont+=1
while n<cpu:
    n=int(input('É MAIS do que isso, me diga outro chute: '))
    cont+=1
print('Você acertou depois de {} tentativas'.format(cont))
