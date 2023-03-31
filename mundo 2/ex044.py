print('{:=^40}' .format(' LOJAS BANANAS '))
preco=float(input('Preço das compras: R$'))
print('''Método de pagamento:
[1] à vista dinheiro
[2] à vista no cartão
[3] cartão 2x
[4] cartão 3x ou mais''')
opcao=int(input('Qual a opção? '))
if opcao==1:
    preco=preco*0.90
    print('O valor final é de R${}'.format(preco))
elif opcao==2:
    preco=preco*0.95
    print('O valor final é de R${}'.format(preco))
elif opcao==3:
    preco=preco
    print('O valor final é de R${}'.format(preco))
elif opcao==4:
    preco=preco*1.10
    print('O valor final é de R${}'.format(preco))
else:
    print('Não existe essa opção')

