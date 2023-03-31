termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão da PA: '))
cont=0
total=0
amais=10
while amais!=0:
    total+=amais    
    while cont<=total:
        print('{} - '.format(termo), end='')
        termo+=razao
        cont+=1
    print('PAUSA')
    amais=int(input('Quantos você deseja mostrar a mais? '))
print('Proressão finalizada com {} termos mostrados'.format(total))
