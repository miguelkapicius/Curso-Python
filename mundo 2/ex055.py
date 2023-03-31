menor=0
maior=0
for pess in range(1,6):
    peso=float(input('Digite o peso da {}° pessoa: '.format(pess)))
    if pess==1:
        menor=peso
        maior=peso
    else:
        if peso> maior:
            maior=peso
        if peso< menor:
            menor=peso
print('O maior peso lido foi {}kg e o menor foi {}kg'.format(maior, menor))
