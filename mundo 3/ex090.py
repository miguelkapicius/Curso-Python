aluno= {}
aluno['Nome']=str(input('Nome: ')).strip()
aluno['Média']=float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média']<=3:
    aluno['Situação']='Reprovado'

elif aluno['Média']< 7:
    aluno['Situação']='Recuperação'

elif aluno['Média]']>=7:
    aluno['Situação']='Aprovado'

print('-='*20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print('-='*20)