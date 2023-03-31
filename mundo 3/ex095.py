time=[]
jogador={}
gols=[]
soma=0

while True:
    jogador['nome']=str(input('Nome do Jogador: ')).strip()
    partidas= int(input(f'Quantas partidas {jogador["nome"]} jogou? ' ))
    for p in range(0,partidas):
        g= int(input(f'Quantos gols na partida {p+1}? '))
        gols.append(g)
    soma=+g
    jogador['gols'] = gols[:]
    jogador['total'] = soma
    time.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite só S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)

while True:
    busca= int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'O número {busca} não existe, por favor digite um número válido.')
    else:
        print(f'Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate (time[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-='*30)

print('<<VOLTE SEMPRE>>')