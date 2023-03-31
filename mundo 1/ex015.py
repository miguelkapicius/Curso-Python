dias=int(input('Quantos dias o carro foi lugado? '))
km=float(input('Quantos Km foram rodados? '))
precd= dias*60
preck= km*0.15
final= precd+preck
print('O valor total a pagar é de R${}'.format(final))
