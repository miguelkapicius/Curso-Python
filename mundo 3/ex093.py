jogador={}
gols=[]
soma=0
jogador['nome']=str(input('Nome do Jogador: ')).strip()
partidas= int(input(f'Quantas partidas {jogador["nome"]} jogou? ' ))
for p in range(0,partidas):
    g= int(input(f'Quantos gols na partida {p}? '))
    gols.append(g)
    soma+=g

jogador['gols'] = gols[:]
jogador['total'] = soma
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, a in enumerate(gols):
    print(f'Na partida {i}, fez {a} gols')
print(f'Foi um total de {soma} gols')