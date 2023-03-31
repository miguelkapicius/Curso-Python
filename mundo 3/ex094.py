banco = []
mulheres = []
idoso = []
cadastro = {}
cont = soma = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
    
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
    
    cadastro['idade'] = int(input('Idade: '))
    cont+=1
    soma += cadastro["idade"]
    
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro.copy())
    if cadastro['idade'] >= 60:
        idoso.append(cadastro.copy())
    
    banco.append(cadastro.copy())
    r=str(input('Quer continuar? [S/N] ')).upper()
    
    while r not in 'SN':
        r=str(input('Quer continuar? [S/N] ')).upper()
        print('ERRO! Por favor, digite apenas S ou N.')
    
    if r =='N':
        break

media = soma/cont
print('-='*30)
print(f'Foram cadastradas {cont} pessoas, e a média de idade é {media}.')
print('-='*30)
print(f'As mulheres são: {mulheres}')
print('-='*30)
print(f'Os idosos são: {idoso}')