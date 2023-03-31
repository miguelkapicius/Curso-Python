soma=0
cont=0
for valores in range(1,501, 2):
    if valores % 3 == 0:
        cont=cont+1
        soma=soma+valores
print('A soma de todos os {} valores é {}'.format(cont, soma))
