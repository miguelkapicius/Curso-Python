print('~'*30)
print('{:^30}'.format('CADASTRE PESSOAS'))
print('~'*30)
idade=sexo=continuar=cont18=contM=contF=0
while True:
    idade=int(input('Digite a idade: '))
    sexo=str(input('Digite o sexo [M/F]: ')).upper().strip()
    print('-'*30)
    if idade>=18:
        cont18+=1
    if sexo=='M':
        contM+=1
    if sexo=='F' and idade<20:
        contF+=1
    continuar=str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar=='N':
        break
print(f'''
Total de pessoas com mais de 18 anos: {cont18}
Ao todo temos {contM} homens cadastrados
Temos {contF} com menos de 20 anos''')