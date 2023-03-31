lista=[[], [], [], []]
while True:
    nome=str(input('Digite o nome do aluno: ')).upper().strip()
    n1=float(input(f'Digite a primeira nota de {nome}: '))
    n2=float(input(f'Digite a segunda nota de {nome}: '))
    media= (n1+n2)/2
    lista.append([nome, [n1,n2], media])
    r=str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, p in enumerate(lista):
    print(f'{i}, {p[0]}, {p[2]}' )