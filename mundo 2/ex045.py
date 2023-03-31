from random import randint
itens = ('Pedra','Papel','Tesoura')
cpu= randint(0,2)
print('''
[0] pedra
[1] papel
[2] tesoura''')
jogador=int(input('Qual a sua jogada? '))
print('Jo')
print('Ken')
print('Po!!!')
print('-=' *12)
print('CPU jogou {}'.format(itens[cpu]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *12)
if cpu==0:
    if jogador==1:
        print('Jogador ganha')
    elif jogador==0:
        print('Empate')
    elif jogador==2:
        print('CPU ganha')
elif cpu==1:
    if jogador==1:
        print('Empate')
    elif jogador==0:
        print('CPU ganha')
    elif jogador==2:
        print('Jogador ganha')
elif cpu==2:
    if jogador==0:
        print('Jogador ganha')
    elif jogador==1:
        print('CPU ganha')
    elif jogador==2:
        print('Empate')
