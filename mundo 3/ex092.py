pessoa={}
pessoa['Nome'] =str(input('Nome: '))
nascimento=int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
pessoa['Idade'] = 2023 - nascimento   
if pessoa['CTPS'] != 0:
    pessoa['Contratação']=int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    trabalho = 54 - (2023 - pessoa['Contratação'])
    pessoa['Aposentadoria'] = pessoa['Idade'] + trabalho

print('-='*25)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
