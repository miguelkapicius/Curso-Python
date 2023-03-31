sal=float(input('Qual o salário? '))
if sal>1250:
    valor= sal*0.10
else:
    valor= sal*0.15
final= valor+sal
print('O valor final é R${}'.format(final))
