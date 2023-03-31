sexo=str(input('Digite o sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo=str(input('Digite um sexo válido [M,F]: ')).upper().strip()[0]
print('ACABOU!!!')